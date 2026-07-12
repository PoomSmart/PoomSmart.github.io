import json
import re
import subprocess
from functools import lru_cache
from pathlib import Path

from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError


root = Path(__file__).resolve().parent
repo_dir = root.parent
data_dir = repo_dir / "data"
schema_path = data_dir / "schema.json"

DEPICTION_URL_PATTERN = re.compile(
    r"https://poomsmart\.github\.io/repo/depictions/([^.]+)\.html"
)

CATEGORY_NAMES = ("core", "youtube", "emoji", "camera", "springboard", "app")
REQUIRED_ENTRY_KEYS = ("file", "title", "description")
OPTIONAL_STRING_KEYS = (
    "min_ios",
    "max_ios",
    "description",
    "extra_content",
    "headerImage",
    "tintColor",
    "backgroundColor",
)
OPTIONAL_BOOL_KEYS = (
    "strict_range",
    "screenshots",
    "featured_as_banner",
    "inline_source_code",
    "link_source_code",
    "no_sileo",
    "debug",
)


class DepictionSchemaError(ValueError):
    pass


@lru_cache(maxsize=1)
def _load_schema():
    with schema_path.open(encoding="utf-8") as handle:
        return json.load(handle)


@lru_cache(maxsize=1)
def _entry_validator():
    schema = _load_schema()
    entry_schema = {"$ref": "#/$defs/entry", "$defs": schema["$defs"]}
    return Draft202012Validator(entry_schema)


@lru_cache(maxsize=1)
def _category_validator():
    return Draft202012Validator(_load_schema())


def _raise_schema_error(error):
    path = ".".join(str(segment) for segment in error.absolute_path)
    location = f" at '{path}'" if path else ""
    raise DepictionSchemaError(f"Schema validation failed{location}: {error.message}") from error


def validate_entry(entry):
    try:
        _entry_validator().validate(entry)
    except ValidationError as error:
        _raise_schema_error(error)


def _load_json_file(name):
    file_path = data_dir / f"{name}.json"
    with file_path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_category(name):
    entries = _load_json_file(name)
    try:
        _category_validator().validate(entries)
    except ValidationError as error:
        _raise_schema_error(error)
    return entries


def load_all_tweaks():
    tweaks = []
    for name in CATEGORY_NAMES:
        tweaks.extend(load_category(name))
    return tweaks


def validate_all_categories():
    for name in CATEGORY_NAMES:
        load_category(name)


class DebCoverageError(ValueError):
    pass


def _parse_deb_index(debs_dir: Path) -> dict[str, str]:
    """Return a ``slug → latest_version`` mapping by running ``dpkg-scanpackages``.

    Uses ``dpkg-scanpackages`` without ``-m`` so only the highest version of each
    (Package, Architecture) pair is emitted — one fast process call.

    Slug resolution per stanza:
    1. Prefer the package whose suffix **exactly matches** the depiction slug
       (e.g. ``com.ps.sfsymbols`` → slug ``sfsymbols``, version ``1.0.10``).
    2. Fall back to the depiction slug from the URL when no exact-suffix match
       exists for that slug (e.g. ``daniel.analytics`` → slug ``osanalytics``).
    3. Last resort: the package-name suffix with no depiction URL.

    Priority prevents companion packages that share a depiction URL (e.g.
    ``com.ps.sfsymbolsassets`` also pointing at ``sfsymbols.html``) from
    overwriting the version recorded for the primary package.
    """
    result = subprocess.run(
        ["dpkg-scanpackages", str(debs_dir), "/dev/null"],
        capture_output=True,
        text=True,
    )

    # Maps slug → (version, is_exact_match)
    _slug_info: dict[str, tuple[str, bool]] = {}

    def _commit(pkg: str, version: str, depiction_slug: str, pkg_suffix: str) -> None:
        if not (pkg and version):
            return
        # Exact match: the package suffix is the same as the depiction slug
        exact = bool(depiction_slug) and pkg_suffix == depiction_slug
        for slug in filter(None, {depiction_slug, pkg_suffix}):
            existing = _slug_info.get(slug)
            if existing is None or (not existing[1] and exact):
                _slug_info[slug] = (version, exact or slug == pkg_suffix)

    pkg = version = depiction_slug = pkg_suffix = ""
    for line in result.stdout.splitlines():
        if not line:
            _commit(pkg, version, depiction_slug, pkg_suffix)
            pkg = version = depiction_slug = pkg_suffix = ""
        elif line.startswith("Package:"):
            pkg = line.split(":", 1)[1].strip()
            pkg_suffix = pkg.rsplit(".", 1)[-1]
        elif line.startswith("Version:"):
            version = line.split(":", 1)[1].strip()
        elif line.startswith("Depiction:"):
            url = line.split(":", 1)[1].strip()
            m = DEPICTION_URL_PATTERN.match(url)
            if m:
                depiction_slug = m.group(1)

    _commit(pkg, version, depiction_slug, pkg_suffix)  # trailing stanza

    return {slug: ver for slug, (ver, _) in _slug_info.items()}


def validate_deb_coverage(debs_dir: Path | None = None) -> None:
    """Raise DebCoverageError if any data entry has no matching .deb or stale changelog.

    Only the **newest** version of each (package, arch) pair is inspected.

    Two checks are run for every entry:
    1. **Coverage** — a deb package matching the entry's slug must exist.
    2. **Changelog currency** — if the entry has a ``changes`` list, its first
       (newest) version must equal the latest deb version, ensuring that a new
       deb release is always accompanied by a changelog update.
    """
    if debs_dir is None:
        debs_dir = repo_dir / "debs"

    if not debs_dir.is_dir():
        raise DebCoverageError(f"debs directory not found at {debs_dir}.")

    slug_to_version = _parse_deb_index(debs_dir)

    missing: list[str] = []
    stale: list[str] = []

    for category in CATEGORY_NAMES:
        for entry in load_category(category):
            slug = entry["file"]
            if slug not in slug_to_version:
                missing.append(f"  [{category}] {slug!r} (title: {entry['title']!r})")
                continue

            changes = entry.get("changes")
            if changes:
                deb_ver = slug_to_version[slug]
                log_ver = changes[0]["version"]
                if log_ver != deb_ver:
                    stale.append(
                        f"  [{category}] {slug!r}: "
                        f"deb is {deb_ver!r} but changelog starts at {log_ver!r}"
                    )

    errors: list[str] = []
    if missing:
        errors.append(
            "The following data entries have no matching .deb package:\n"
            + "\n".join(missing)
        )
    if stale:
        errors.append(
            "The following entries have a changelog that does not match the latest deb version:\n"
            + "\n".join(stale)
        )
    if errors:
        raise DebCoverageError("\n\n".join(errors))
