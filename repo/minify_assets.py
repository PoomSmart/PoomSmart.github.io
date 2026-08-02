from pathlib import Path

import rcssmin
import rjsmin

SITE_ROOT = Path(__file__).resolve().parent.parent

JS_FILES = (
    ("misc/iosver.js", "misc/iosver.min.js"),
    ("assets/emojiport.js", "assets/emojiport.min.js"),
)

CSS_FILES = (
    ("assets/misc.css", "assets/misc.min.css"),
    ("assets/site.css", "assets/site.min.css"),
    ("assets/emojiport.css", "assets/emojiport.min.css"),
)


def minify_js(source_path, output_path):
    source = source_path.read_text(encoding="utf-8")
    output = rjsmin.jsmin(source, keep_bang_comments=True)
    output_path.write_text(output + "\n", encoding="utf-8")


def minify_css(source_path, output_path):
    source = source_path.read_text(encoding="utf-8")
    output = rcssmin.cssmin(source, keep_bang_comments=True)
    output_path.write_text(output + "\n", encoding="utf-8")


def main():
    for source_rel, output_rel in JS_FILES:
        source_path = SITE_ROOT / source_rel
        output_path = SITE_ROOT / output_rel

        if not source_path.exists():
            raise FileNotFoundError(f"JavaScript source not found: {source_path}")

        minify_js(source_path, output_path)
        print(f"Minified {source_rel} -> {output_rel}")

    for source_rel, output_rel in CSS_FILES:
        source_path = SITE_ROOT / source_rel
        output_path = SITE_ROOT / output_rel

        if not source_path.exists():
            raise FileNotFoundError(f"CSS source not found: {source_path}")

        minify_css(source_path, output_path)
        print(f"Minified {source_rel} -> {output_rel}")


if __name__ == "__main__":
    main()
