import json
import re
from dataclasses import dataclass
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
IOS_RANGE_PATTERN = re.compile(
    r"^\[(?P<min>\d+(?:\.\d+){0,2}),\s*"
    r"(?:(?P<max>\d+(?:\.\d+){0,2})(?P<bound>[)\]])|(?P<open>\)))"
    r"(?P<strict>!)?$"
)

CATEGORY_NAMES = ("core", "youtube", "emoji", "camera", "springboard", "app")

# iOS 26 follows iOS 18. Majors 19 through 25 were never released.
_UNRELEASED_IOS_MAJORS = range(19, 26)


class DepictionSchemaError(ValueError):
    pass


@dataclass(frozen=True)
class IosRange:
    min: str
    max: str | None = None
    max_exclusive: bool = False
    strict: bool = False

    def label(self) -> str:
        if self.max is None:
            return f"Compatible with iOS {self.min} +"
        if self.max_exclusive:
            max_major = int(self.max.split(".", 1)[0])
            if max_major >= 1:
                display_major = _previous_ios_major(max_major)
                min_major = int(self.min.split(".", 1)[0])
                if min_major == display_major:
                    return f"Compatible with iOS {display_major}.x"
                return f"Compatible with iOS {self.min} to {display_major}.x"
            return f"Compatible with iOS {self.min} before {self.max}"
        return f"Compatible with iOS {self.min} to {self.max}"


def _previous_ios_major(major: int) -> int:
    """Last released major covered by an exclusive upper bound of ``major``.

    ``[14.0, 26.0)`` reaches through 18.x, because 19 through 25 do not exist.
    """
    previous = major - 1
    if previous in _UNRELEASED_IOS_MAJORS:
        return 18
    return previous


def parse_ios_range(value: str) -> IosRange:
    """Parse interval notation such as ``[11.0,)``, ``[8.0, 18.0]``, ``[12.0, 17.0]!``."""
    match = IOS_RANGE_PATTERN.fullmatch(value)
    if not match:
        raise DepictionSchemaError(
            f"Invalid ios range {value!r}; expected e.g. '[11.0,)', '[8.0, 18.0]', '[12.0, 17.0)!'"
        )

    min_ios = match.group("min")
    max_ios = match.group("max")
    strict = match.group("strict") is not None

    if max_ios is None:
        if strict:
            raise DepictionSchemaError(
                f"Invalid ios range {value!r}: '!' requires an upper bound"
            )
        return IosRange(min=min_ios)

    return IosRange(
        min=min_ios,
        max=max_ios,
        max_exclusive=match.group("bound") == ")",
        strict=strict,
    )


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


def _validate_ios(entry):
    if "ios" in entry:
        parse_ios_range(entry["ios"])


def validate_entry(entry):
    try:
        _entry_validator().validate(entry)
    except ValidationError as error:
        _raise_schema_error(error)
    _validate_ios(entry)


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
    for entry in entries:
        _validate_ios(entry)
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


def _slug_versions(records) -> dict[str, str]:
    """Return ``slug → latest_version`` from deb records.

    Keeps the highest dpkg version of each package name. Slug resolution:
    1. Prefer the package whose suffix exactly matches the depiction slug
       (e.g. ``com.ps.sfsymbols`` → slug ``sfsymbols``).
    2. Fall back to the depiction slug from the URL when no exact-suffix match
       exists (e.g. ``daniel.analytics`` → slug ``osanalytics``).
    3. Last resort: the package-name suffix with no depiction URL.

    An exact suffix match is kept over a companion package that only shares
    the depiction URL (e.g. ``com.ps.sfsymbolsassets`` also pointing at
    ``sfsymbols.html``).
    """
    try:
        from .deb_index import version_compare
    except ImportError:
        from deb_index import version_compare

    winners = {}
    for record in records:
        current = winners.get(record.package)
        if current is None or version_compare(record.version, current.version) > 0:
            winners[record.package] = record

    # slug → (version, is_exact_match)
    slug_info: dict[str, tuple[str, bool]] = {}

    def commit(pkg: str, version: str, depiction_slug: str, pkg_suffix: str) -> None:
        if not (pkg and version):
            return
        exact = bool(depiction_slug) and pkg_suffix == depiction_slug
        for slug in filter(None, {depiction_slug, pkg_suffix}):
            existing = slug_info.get(slug)
            if existing is None or (not existing[1] and exact):
                slug_info[slug] = (version, exact or slug == pkg_suffix)

    for package in sorted(winners):
        record = winners[package]
        depiction_slug = ""
        match = DEPICTION_URL_PATTERN.match(record.depiction)
        if match:
            depiction_slug = match.group(1)
        commit(package, record.version, depiction_slug, package.rsplit(".", 1)[-1])

    return {slug: version for slug, (version, _) in slug_info.items()}


def validate_deb_coverage(debs_dir: Path | None = None, records=None) -> None:
    """Raise DebCoverageError if any data entry has no matching .deb or stale changelog.

    Only the newest version of each package name is inspected.

    Two checks are run for every entry:
    1. **Coverage** — a deb package matching the entry's slug must exist.
    2. **Changelog currency** — if the entry has a ``changes`` list, its first
       (newest) version must equal the latest deb version, ensuring that a new
       deb release is always accompanied by a changelog update.
    """
    if records is None:
        if debs_dir is None:
            debs_dir = repo_dir / "debs"
        if not debs_dir.is_dir():
            raise DebCoverageError(f"debs directory not found at {debs_dir}.")
        try:
            from .deb_index import scan_debs
        except ImportError:
            from deb_index import scan_debs

        records = scan_debs(debs_dir)

    slug_to_version = _slug_versions(records)

    missing: list[str] = []
    stale: list[str] = []

    for category in CATEGORY_NAMES:
        for entry in load_category(category):
            slug = entry["file"]
            if slug not in slug_to_version:
                missing.append(f"  [{category}] {slug!r} (title: {entry['title']!r})")
                continue

            if entry.get("no_changelog"):
                continue

            deb_ver = slug_to_version[slug]
            changes = entry.get("changes")
            if not changes:
                stale.append(
                    f"  [{category}] {slug!r}: "
                    f"deb is {deb_ver!r} but entry has no changelog"
                )
            elif changes[0]["version"] != deb_ver:
                stale.append(
                    f"  [{category}] {slug!r}: "
                    f"deb is {deb_ver!r} but changelog starts at {changes[0]['version']!r}"
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
