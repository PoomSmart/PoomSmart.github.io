from gen.data_loader import validate_all_categories, validate_deb_coverage


def main():
    validate_all_categories()
    print("Metadata schema validation passed")
    validate_deb_coverage()
    print("Deb coverage validation passed")


if __name__ == "__main__":
    main()