import json
from functools import lru_cache
from pathlib import Path

from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError


root = Path(__file__).resolve().parent
data_dir = root.parent / "data"
schema_path = data_dir / "schema.json"

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
