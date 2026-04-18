import html
import json
import re
from pathlib import Path

import minify_html
from jinja2 import Environment, FileSystemLoader


root = Path(__file__).resolve().parent
repo_root = root.parent
templates_dir = repo_root / "templates"
screenshots_dir = repo_root / "screenshots"
depictions_dir = repo_root / "depictions"
sileo_depictions_dir = repo_root / "sileodepictions"

env = Environment(loader=FileSystemLoader(templates_dir), trim_blocks=True, lstrip_blocks=True)
html_template = env.get_template("index.html")
source_template_path = templates_dir / "index.json"

SOURCE_CODE_FOLDERS = ("SpringBoard", "YouTube", "Camera")
SILEO_KEYS = ("headerImage", "tintColor", "backgroundColor")


class DepictionAssetError(FileNotFoundError):
    pass


def normalize_markup(value):
    value = value.strip()
    value = re.sub(r">\s+<", "><", value)
    return re.sub(r"\s{2,}", " ", value)


def warn(message):
    print(f"Warning: {message}")


def collect_screenshots(file_name, strict=False):
    screenshot_dir = screenshots_dir / file_name
    if not screenshot_dir.exists():
        message = f"Screenshots directory for {file_name} not found"
        if strict:
            raise DepictionAssetError(message)
        warn(message)
        return []

    return [
        {
            "url": f"https://poomsmart.github.io/repo/screenshots/{file_name}/{entry.name}",
            "accessibilityText": entry.name,
        }
        for entry in sorted(screenshot_dir.iterdir(), key=lambda item: item.name)
        if not entry.name.startswith(".") and entry.is_file()
    ]


def load_inline_source_code(file_name, title, strict=False):
    for folder in SOURCE_CODE_FOLDERS:
        source_code_path = (root / f"../../{folder}/{file_name}/Tweak.x").resolve()
        if source_code_path.exists():
            try:
                return source_code_path.read_text(encoding="utf-8")
            except OSError:
                message = f"Could not read source code of {title}"
                if strict:
                    raise DepictionAssetError(message)
                warn(message)
                return None

    message = f"Source code of {title} not found"
    if strict:
        raise DepictionAssetError(message)
    warn(message)
    return None


def build_sileo_depiction(entry, description, extra_content, screenshots, source_code):
    with source_template_path.open(encoding="utf-8") as json_file:
        data = json.load(json_file)

    for key in SILEO_KEYS:
        value = entry.get(key)
        if value:
            data[key] = value

    if entry.get("featured_as_banner") and "headerImage" not in entry:
        data["headerImage"] = f"https://poomsmart.github.io/repo/features/{entry['file']}.png"

    tabs = data["tabs"]
    detail_views = None
    for tab in tabs:
        if tab["tabname"] != "Details":
            continue
        detail_views = tab["views"]
        detail_views[0]["markdown"] = description
        if screenshots:
            detail_views.insert(0, {
                "class": "DepictionScreenshotsView",
                "itemCornerRadius": 14,
                "screenshots": screenshots,
                "itemSize": "{160,284}",
            })
        if extra_content:
            detail_views.append({
                "class": "DepictionMarkdownView",
                "markdown": extra_content,
                "useSpacing": True,
                "useRawFormat": True,
            })

    min_ios = entry.get("min_ios")
    max_ios = entry.get("max_ios")
    if detail_views and min_ios:
        detail_views.insert(0, {
            "class": "DepictionSubheaderView",
            "useMargins": True,
            "title": f"Compatible with iOS {min_ios} to {max_ios}" if min_ios and max_ios else f"Compatible with iOS {min_ios} +",
        })

    if source_code:
        tabs.append({
            "class": "DepictionStackView",
            "tabname": "Source Code",
            "views": [{
                "class": "DepictionMarkdownView",
                "markdown": f"```\n{source_code}\n```",
            }],
        })

    changes = entry.get("changes")
    if changes:
        change_views = []
        first_change = True
        for version, details in changes:
            if not first_change:
                change_views.append({"class": "DepictionSeparatorView"})
            change_views.append({
                "class": "DepictionSubheaderView",
                "title": f"Version {version}",
            })
            if isinstance(details, list):
                markdown = "".join(f"- {item}\n" for item in details)
            else:
                markdown = f"- {details}"
            change_views.append({
                "class": "DepictionMarkdownView",
                "markdown": markdown,
            })
            first_change = False
        tabs.append({
            "class": "DepictionStackView",
            "tabname": "Changelog",
            "views": change_views,
        })

    return data


def generate_depictions(entries, strict=False):
    generated_count = 0
    for entry in entries:
        file_name = entry["file"]
        title = entry["title"]
        description = normalize_markup(entry["description"])
        extra_content = entry.get("extra_content")
        if extra_content:
            extra_content = normalize_markup(extra_content)

        screenshots = collect_screenshots(file_name, strict=strict) if entry.get("screenshots") else []
        source_code = None
        if entry.get("inline_source_code"):
            source_code = load_inline_source_code(file_name, title, strict=strict)
            if source_code is None:
                continue

        html_output = minify_html.minify(html_template.render(
            title=title,
            min_ios=entry.get("min_ios"),
            max_ios=entry.get("max_ios"),
            strict_range=entry.get("strict_range"),
            changes=entry.get("changes"),
            screenshots=screenshots,
            description=description,
            extra_content=extra_content,
            source_code=html.escape(source_code) if source_code is not None else None,
            debug=entry.get("debug"),
        ), minify_js=False, minify_css=False)
        output_path = depictions_dir / f"{file_name}.html"
        output_path.write_text(html_output, encoding="utf-8")
        print(f"Generated {output_path}")
        generated_count += 1

        if entry.get("no_sileo"):
            continue

        sileo_output_path = sileo_depictions_dir / f"{file_name}.json"
        sileo_data = build_sileo_depiction(entry, description, extra_content, screenshots, source_code)
        with sileo_output_path.open("w", encoding="utf-8") as out_file:
            json.dump(sileo_data, out_file)
        print(f"Generated {sileo_output_path}")

    return generated_count
