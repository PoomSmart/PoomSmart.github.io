import json
from pathlib import Path


root = Path(__file__).resolve().parent
data_dir = root.parent / "data"

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


def validate_entry(entry):
    if not isinstance(entry, dict):
        raise DepictionSchemaError("Each tweak entry must be an object")

    missing_keys = [key for key in REQUIRED_ENTRY_KEYS if not entry.get(key)]
    if missing_keys:
        raise DepictionSchemaError(f"Entry is missing required keys: {', '.join(missing_keys)}")

    for key in REQUIRED_ENTRY_KEYS + OPTIONAL_STRING_KEYS:
        value = entry.get(key)
        if value is not None and not isinstance(value, str):
            raise DepictionSchemaError(f"Entry field '{key}' must be a string")

    for key in OPTIONAL_BOOL_KEYS:
        value = entry.get(key)
        if value is not None and not isinstance(value, bool):
            raise DepictionSchemaError(f"Entry field '{key}' must be a boolean")

    changes = entry.get("changes")
    if changes is None:
        return

    if not isinstance(changes, list):
        raise DepictionSchemaError("Entry field 'changes' must be a list")

    for change in changes:
        if not isinstance(change, list) or len(change) != 2 or not isinstance(change[0], str):
            raise DepictionSchemaError("Each changelog item must be a two-item list starting with a version string")

        details = change[1]
        if isinstance(details, str):
            continue
        if isinstance(details, list) and all(isinstance(item, str) for item in details):
            continue
        raise DepictionSchemaError("Each changelog detail must be a string or a list of strings")


def _load_json_file(name):
    file_path = data_dir / f"{name}.json"
    with file_path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_category(name):
    entries = _load_json_file(name)
    if not isinstance(entries, list):
        raise DepictionSchemaError(f"Category '{name}' must load as a list")
    for entry in entries:
        validate_entry(entry)
    return entries


def load_all_tweaks():
    tweaks = []
    for name in CATEGORY_NAMES:
        tweaks.extend(load_category(name))
    return tweaks
