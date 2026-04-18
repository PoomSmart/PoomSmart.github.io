from gen.data_loader import validate_all_categories


def main():
    validate_all_categories()
    print("Metadata schema validation passed")


if __name__ == "__main__":
    main()