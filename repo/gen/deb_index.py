"""Build a dpkg-scanpackages-compatible Packages index without forking per deb."""

import hashlib
import io
import os
import re
import tarfile
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path

# Field order of Dpkg::Control CTRL_REPO_PKG (dpkg 1.23).
_REPO_FIELDS = (
    "Package",
    "Package-Type",
    "Source",
    "Version",
    "Kernel-Version",
    "Built-For-Profiles",
    "Auto-Built-Package",
    "Architecture",
    "Subarchitecture",
    "Installer-Menu-Item",
    "Build-Essential",
    "Essential",
    "Protected",
    "Origin",
    "Bugs",
    "Maintainer",
    "Installed-Size",
    "Pre-Depends",
    "Depends",
    "Recommends",
    "Suggests",
    "Enhances",
    "Conflicts",
    "Breaks",
    "Replaces",
    "Provides",
    "Built-Using",
    "Static-Built-Using",
    "Filename",
    "Size",
    "MD5sum",
    "SHA1",
    "SHA256",
    "Section",
    "Priority",
    "Multi-Arch",
    "Homepage",
    "Description",
    "Tag",
    "Task",
)
_OFFICIAL_NAMES = {name.lower(): name for name in _REPO_FIELDS}
_DIGIT_BOUNDARY = re.compile(r"(?<=\d)(?=\D)|(?<=\D)(?=\d)")


@dataclass(frozen=True)
class DebRecord:
    package: str
    version: str
    depiction: str
    fields: dict[str, str]


def version_compare(left: str, right: str) -> int:
    """Return -1, 0, or 1 using dpkg version ordering."""
    for part_left, part_right in zip(_split_version(left), _split_version(right), strict=True):
        compared = _compare_part(part_left, part_right)
        if compared:
            return compared
    return 0


def scan_debs(debs_dir: Path) -> list[DebRecord]:
    """Read every .deb once and return records in File::Find order."""
    debs_dir = Path(debs_dir)
    if not debs_dir.is_dir():
        raise FileNotFoundError(f"debs directory not found at {debs_dir}")

    paths = _find_debs(debs_dir)
    repo_dir = debs_dir.parent
    workers = os.cpu_count() or 1
    with ThreadPoolExecutor(max_workers=workers) as executor:
        return list(executor.map(lambda path: _scan_deb(path, repo_dir), paths))


def format_packages(records: list[DebRecord]) -> str:
    """Render records the way ``dpkg-scanpackages -m`` prints them."""
    ordered = sorted(records, key=lambda record: (record.package, record.version))
    return "".join(f"{_format_stanza(record.fields)}\n" for record in ordered)


def _find_debs(debs_dir: Path) -> list[Path]:
    """Walk like Perl File::Find with follow enabled.

    Files in a directory keep readdir order. Subdirectories are visited
    afterwards, in reverse readdir order.
    """
    found: list[Path] = []

    def walk(directory: Path) -> None:
        with os.scandir(directory) as entries:
            names = [entry.name for entry in entries]
        subdirs: list[Path] = []
        for name in names:
            child = directory / name
            if child.is_dir():
                subdirs.append(child)
            elif name.endswith(".deb"):
                found.append(child)
        for child in reversed(subdirs):
            walk(child)

    walk(debs_dir)
    return found


def _scan_deb(path: Path, repo_dir: Path) -> DebRecord:
    digest_md5 = hashlib.md5()
    digest_sha1 = hashlib.sha1()
    digest_sha256 = hashlib.sha256()
    digests = (digest_md5, digest_sha1, digest_sha256)
    control_member: tuple[str, bytes] | None = None

    with path.open("rb") as handle:
        magic = _read(handle, 8, digests)
        if magic != b"!<arch>\n":
            raise ValueError(f"{path}: not a deb archive")
        while True:
            header = handle.read(60)
            if not header:
                break
            if len(header) != 60:
                raise ValueError(f"{path}: truncated ar header")
            for digest in digests:
                digest.update(header)
            member_size = int(header[48:58])
            name, data_size = _ar_name(handle, header[:16], member_size, digests)
            if name.startswith("control.tar"):
                control_member = (name, _read(handle, data_size, digests))
            else:
                _hash_skip(handle, data_size, digests)
            if member_size % 2:
                _read(handle, 1, digests)

    if control_member is None:
        raise ValueError(f"{path}: missing control.tar member")

    fields = _parse_control(_control_text(*control_member, path))
    relative = path.relative_to(repo_dir).as_posix()
    fields["Filename"] = f"./{relative}"
    fields["Size"] = str(path.stat().st_size)
    fields["MD5sum"] = digest_md5.hexdigest()
    fields["SHA1"] = digest_sha1.hexdigest()
    fields["SHA256"] = digest_sha256.hexdigest()

    package = fields.get("Package", "")
    version = fields.get("Version", "")
    if not package or not version:
        raise ValueError(f"{path}: control file is missing Package or Version")
    return DebRecord(
        package=package,
        version=version,
        depiction=fields.get("Depiction", ""),
        fields=fields,
    )


def _ar_name(handle, raw_name: bytes, member_size: int, digests) -> tuple[str, int]:
    name = raw_name.decode("ascii", "replace")
    if name.startswith("#1/"):
        name_len = int(name[3:])
        name = _read(handle, name_len, digests).decode("utf-8", "replace").rstrip("\x00")
        return name, member_size - name_len
    return name.rstrip(" /"), member_size


def _hash_skip(handle, size: int, digests) -> None:
    remaining = size
    while remaining:
        chunk = handle.read(min(1024 * 1024, remaining))
        if not chunk:
            raise ValueError("truncated deb member")
        for digest in digests:
            digest.update(chunk)
        remaining -= len(chunk)


def _read(handle, size: int, digests) -> bytes:
    data = handle.read(size)
    if len(data) != size:
        raise ValueError("truncated deb archive")
    for digest in digests:
        digest.update(data)
    return data


def _control_text(name: str, payload: bytes, path: Path) -> str:
    if name.endswith(".gz"):
        mode = "r:gz"
    elif name.endswith(".xz"):
        mode = "r:xz"
    elif name.endswith(".bz2"):
        mode = "r:bz2"
    else:
        raise ValueError(f"{path}: unsupported control member {name}")
    with tarfile.open(fileobj=io.BytesIO(payload), mode=mode) as archive:
        for member in archive.getmembers():
            if member.name.rsplit("/", 1)[-1] != "control":
                continue
            extracted = archive.extractfile(member)
            if extracted is None:
                break
            return extracted.read().decode("utf-8")
    raise ValueError(f"{path}: control archive has no control file")


def _parse_control(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    current: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line:
            if current is not None:
                break
            continue
        if line.startswith("#"):
            continue
        if line[0].isspace():
            if current is None:
                raise ValueError("continued value line not in a field")
            continued = line[1:]
            if continued and set(continued) <= {"."}:
                continued = continued[1:]
            fields[current] += f"\n{continued}"
            continue
        name, separator, value = line.partition(":")
        if not separator or not name or any(char.isspace() for char in name):
            raise ValueError(f"invalid control line: {raw_line!r}")
        current = _field_capitalize(name)
        if current in fields:
            raise ValueError(f"duplicate control field {current}")
        fields[current] = value.lstrip(" \t")
    return fields


def _field_capitalize(name: str) -> str:
    key = name.lower()
    official = _OFFICIAL_NAMES.get(key)
    if official:
        return official
    return "-".join(part.capitalize() for part in key.split("-"))


def _format_stanza(fields: dict[str, str]) -> str:
    lines: list[str] = []
    emitted: set[str] = set()
    for name in _REPO_FIELDS:
        value = fields.get(name)
        if value is not None and value.strip():
            lines.append(_format_field(name, value))
            emitted.add(name)
    for name in sorted(set(fields) - emitted):
        value = fields[name]
        if value.strip():
            lines.append(_format_field(name, value))
    return "".join(lines)


def _format_field(name: str, value: str) -> str:
    first, *rest = value.split("\n")
    rendered = f"{name}: {first}\n" if first else f"{name}:\n"
    for line in rest:
        if not line or set(line) <= {"."}:
            rendered += f" .{line}\n"
        else:
            rendered += f" {line}\n"
    return rendered


def _split_version(version: str) -> tuple[str, str, str]:
    epoch = "0"
    rest = version
    if ":" in version:
        epoch, rest = version.split(":", 1)
    if "-" in rest:
        upstream, revision = rest.rsplit("-", 1)
    else:
        upstream, revision = rest, "0"
    return epoch, upstream, revision


def _compare_part(left, right) -> int:
    left_parts = _DIGIT_BOUNDARY.split(str(left)) if str(left) != "" else []
    right_parts = _DIGIT_BOUNDARY.split(str(right)) if str(right) != "" else []
    index = 0
    while True:
        left_done = index >= len(left_parts)
        right_done = index >= len(right_parts)
        if left_done and right_done:
            return 0
        left_part = 0 if left_done or left_parts[index] == "" else left_parts[index]
        right_part = 0 if right_done or right_parts[index] == "" else right_parts[index]
        if _is_numeric(left_part) and _is_numeric(right_part):
            left_number = int(left_part)
            right_number = int(right_part)
            if left_number != right_number:
                return 1 if left_number > right_number else -1
        else:
            compared = _compare_string(str(left_part), str(right_part))
            if compared:
                return compared
        index += 1


def _is_numeric(part) -> bool:
    return isinstance(part, int) or (isinstance(part, str) and part.isdigit())


def _compare_string(left: str, right: str) -> int:
    left_orders = [_char_order(char) for char in left]
    right_orders = [_char_order(char) for char in right]
    index = 0
    while True:
        if index >= len(left_orders) and index >= len(right_orders):
            return 0
        left_order = left_orders[index] if index < len(left_orders) else 0
        right_order = right_orders[index] if index < len(right_orders) else 0
        if left_order != right_order:
            return 1 if left_order > right_order else -1
        index += 1


def _char_order(char: str) -> int:
    if char == "~":
        return -1
    if char.isdigit():
        return int(char) + 1
    if char.isalpha():
        return ord(char)
    return ord(char) + 256
