from pathlib import Path
import runpy
import sys


def main():
    repo_root = Path(__file__).resolve().parent
    gen_dir = repo_root / "gen"
    depiction_script = gen_dir / "depiction.py"

    sys.path.insert(0, str(gen_dir))
    try:
        runpy.run_path(str(depiction_script), run_name="__main__")
    finally:
        sys.path.pop(0)


if __name__ == "__main__":
    main()
