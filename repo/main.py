import sys
from pathlib import Path


def main():
    repo_root = Path(__file__).resolve().parent
    gen_dir = repo_root / "gen"

    sys.path.insert(0, str(gen_dir))
    try:
        from depiction import main as depiction_main

        depiction_main()
    finally:
        sys.path.pop(0)


if __name__ == "__main__":
    main()
