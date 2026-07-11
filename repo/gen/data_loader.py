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


def _coverage_sets_from_latest_debs(debs_dir: Path) -> tuple[set[str], set[str]]:
    """Return (depiction_slugs, package_name_suffixes) for the newest deb per package.

    Uses ``dpkg-scanpackages`` without ``-m`` so it naturally outputs only the
    highest version of each (Package, Architecture) pair — one fast process call
    instead of per-file ``dpkg-deb`` invocations.

    depiction_slugs:       slugs from canonical ``Depiction:`` URLs in control files.
    package_name_suffixes: last dot-component of each ``Package:`` field,
                           e.g. ``com.ps.yougetcaption`` → ``yougetcaption``.
    """
    result = subprocess.run(
        ["dpkg-scanpackages", str(debs_dir), "/dev/null"],
        capture_output=True,
        text=True,
    )
    text = result.stdout

    depiction_slugs: set[str] = set()
    package_suffixes: set[str] = set()

    for line in text.splitlines():
        if line.startswith("Package:"):
            pkg = line.split(":", 1)[1].strip()
            package_suffixes.add(pkg.rsplit(".", 1)[-1])
        elif line.startswith("Depiction:"):
            url = line.split(":", 1)[1].strip()
            m = DEPICTION_URL_PATTERN.match(url)
            if m:
                depiction_slugs.add(m.group(1))

    return depiction_slugs, package_suffixes


def validate_deb_coverage(debs_dir: Path | None = None) -> None:
    """Raise DebCoverageError if any data entry has no matching .deb package.

    Only the **newest** version of each (package, arch) pair is inspected.
    A data entry is considered covered when its ``file`` slug either:
    - appears as a depiction slug in a canonical ``Depiction:`` URL, OR
    - matches the last dot-separated component of a ``Package:`` name
      (handles debs whose control file omits the Depiction field).
    """
    if debs_dir is None:
        debs_dir = repo_dir / "debs"

    if not debs_dir.is_dir():
        raise DebCoverageError(f"debs directory not found at {debs_dir}.")

    depiction_slugs, package_suffixes = _coverage_sets_from_latest_debs(debs_dir)
    covered = depiction_slugs | package_suffixes

    missing: list[str] = []
    for category in CATEGORY_NAMES:
        for entry in load_category(category):
            slug = entry["file"]
            if slug not in covered:
                missing.append(f"  [{category}] {slug!r} (title: {entry['title']!r})")

    if missing:
        lines = "\n".join(missing)
        raise DebCoverageError(
            f"The following data entries have no matching .deb package:\n{lines}"
        )
