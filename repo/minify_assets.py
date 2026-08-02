import subprocess
import sys
from pathlib import Path

import rcssmin

REPO_ROOT = Path(__file__).resolve().parent
SITE_ROOT = REPO_ROOT.parent
BUILD_JS = REPO_ROOT / "build_js.mjs"

CSS_FILES = (
    ("assets/misc.css", "assets/misc.min.css"),
    ("assets/site.css", "assets/site.min.css"),
    ("assets/emojiport.css", "assets/emojiport.min.css"),
)


def minify_css(source_path, output_path):
    source = source_path.read_text(encoding="utf-8")
    output = rcssmin.cssmin(source, keep_bang_comments=True)
    output_path.write_text(output + "\n", encoding="utf-8")


def build_js():
    if not BUILD_JS.exists():
        raise FileNotFoundError(f"JavaScript build script not found: {BUILD_JS}")

    subprocess.run(
        ["node", str(BUILD_JS)],
        cwd=REPO_ROOT,
        check=True,
    )


def main():
    build_js()

    for source_rel, output_rel in CSS_FILES:
        source_path = SITE_ROOT / source_rel
        output_path = SITE_ROOT / output_rel

        if not source_path.exists():
            raise FileNotFoundError(f"CSS source not found: {source_path}")

        minify_css(source_path, output_path)
        print(f"Minified {source_rel} -> {output_rel}")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as error:
        sys.exit(error.returncode)
