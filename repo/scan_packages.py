from pathlib import Path

from gen.data_loader import validate_all_categories, validate_deb_coverage
from gen.deb_index import format_packages, scan_debs

REPO_DIR = Path(__file__).resolve().parent


def main():
    validate_all_categories()
    print("Metadata schema validation passed")

    debs_dir = REPO_DIR / "debs"
    records = scan_debs(debs_dir)
    validate_deb_coverage(records=records)
    print("Deb coverage validation passed")

    packages_path = REPO_DIR / "Packages"
    packages_path.write_text(format_packages(records), encoding="utf-8", newline="\n")
    print(f"Wrote {len(records)} entries to Packages")


if __name__ == "__main__":
    main()
