try:
    from .data_loader import DepictionSchemaError, load_all_tweaks, validate_entry
    from .rendering import (
        DepictionAssetError,
        collect_screenshots,
        generate_depictions,
        load_inline_source_code,
    )
except ImportError:
    from data_loader import DepictionSchemaError, load_all_tweaks, validate_entry
    from rendering import (
        DepictionAssetError,
        collect_screenshots,
        generate_depictions,
        load_inline_source_code,
    )


def main(strict=False):
    return generate_depictions(load_all_tweaks(), strict=strict)


__all__ = [
    "DepictionAssetError",
    "DepictionSchemaError",
    "collect_screenshots",
    "generate_depictions",
    "load_all_tweaks",
    "load_inline_source_code",
    "main",
    "validate_entry",
]


if __name__ == "__main__":
    main()
