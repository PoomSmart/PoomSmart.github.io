# follow https://rustup.rs
import html
import json
import re
from pathlib import Path

import minify_html
from jinja2 import Environment, FileSystemLoader

from app import app
from camera import camera
from emoji import emoji
from springboard import springboard
from youtube import youtube

root = Path(__file__).resolve().parent
templates_dir = root / "../templates"
screenshots_dir = root / "../screenshots"
depictions_dir = root / "../depictions"
sileo_depictions_dir = root / "../sileodepictions"
env = Environment(loader=FileSystemLoader(templates_dir), trim_blocks=True, lstrip_blocks=True)
html_template = env.get_template('index.html')

REQUIRED_ENTRY_KEYS = ("file", "title", "description")
SOURCE_CODE_FOLDERS = ("SpringBoard", "YouTube", "Camera")


def normalize_markup(value):
    return re.sub(r'\s+', ' ', value)


def validate_entry(entry):
    missing_keys = [key for key in REQUIRED_ENTRY_KEYS if not entry.get(key)]
    if missing_keys:
        raise ValueError(f"Entry is missing required keys: {', '.join(missing_keys)}")


def collect_screenshots(file_name):
    screenshot_dir = screenshots_dir / file_name
    if not screenshot_dir.exists():
        print(f"Screenshots directory for {file_name} not found")
        return []

    return [
        {
            "url": f"https://poomsmart.github.io/repo/screenshots/{file_name}/{entry.name}",
            "accessibilityText": entry.name,
        }
        for entry in sorted(screenshot_dir.iterdir(), key=lambda item: item.name)
        if not entry.name.startswith('.') and entry.is_file()
    ]


def load_inline_source_code(file_name, title):
    for folder in SOURCE_CODE_FOLDERS:
        source_code_path = (root / f"../../{folder}/{file_name}/Tweak.x").resolve()
        if source_code_path.exists():
            try:
                return source_code_path.read_text(encoding="utf-8")
            except OSError:
                print(f"Could not read source code of {title}")
                return None

    print(f"Source code of {title} not found")
    return None

tweaks = [
    {
        "file": "letmeblock",
        "title": "LetMeBlock",
        "min_ios": "9.0",
        "changes": [
            ["1.3.0", [
                "Fixed jetsam memory limit bypass not working presumably since iOS 9, causing the tweak to have never been working when hosts file is very large",
                "Fixed mDNSResponderHelper not being spawn on modern iOS versions so that the memory limit can be lifted for mDNSResponder",
                "(Rootless) Added libSandy profile to allow access to /var/jb/etc/hosts",
                "Added support for rootless jailbreaks (/var/jb/etc/hosts)",
                "Increased Jetsam memory limit to 512 MB"
            ]]
        ],
        "description": "<p><a target=\"_blank\" href=\"https://github.com/PoomSmart/LetMeBlock/blob/master/README.md\">README</a></p>"
    },
    {
        "file": "smoothkb",
        "title": "SmoothKB",
        "min_ios": "7.0",
        "description": "<p>Fade animation across keyboard typing.</p>"
    },
    {
        "file": "pencilpro",
        "title": "Pencil Pro",
        "min_ios": "9.0",
        "changes": [
            ["1.0.0", "Fixed issues with GoodNotes 5 app"]
        ],
        "description": "<p>A little better Apple Pencil functionalities, even though most of the aimed features are somewhat broken.</p>\
            <p>For more details, visit tweak's <a target=\"_blank\" href=\"https://github.com/PoomSmart/PencilPro/blob/master/README.md\">README</a>.</p>"
    },
    {
        "file": "pearltracking",
        "title": "Pearl Tracking",
        "min_ios": "13.0",
        "description": "<ol>\
            <li>Go to Settings > Control Center > Customize Controls > <i>Enable</i> Pearl Tracking</li>\
            <li>Enable Assistive Touch</li>\
            <li>Invoke Control Center</li>\
            <li><b>Get some painkiller</b></li>\
            <li>Turn on Pearl Tracking</li>\
            <li>???</li>\
        </ol>"
    },
    {
        "file": "hdavatar",
        "title": "HD Avatar",
        "min_ios": "11.0",
        "inline_source_code": True,
        "description": "<p>Default size of Animoji/Memoji stickers is no more than 500px * 500px and the stickers look too pixellated. This tweak will simply double the size.</p>",
        "changes": [
            ["1.0.0", "Supports WWDC 2021 Developer Stickers"]
        ]
    },
    {
        "file": "igclassiclayout",
        "title": "IGClassicLayout",
        "min_ios": "13.0",
        "tintColor": "orange",
        "description": "<p>Restores the original-ish buttons layout in Instagram.</p>",
        "changes": [
            ["1.0.2", "Removed Shopping tab for recent Instagram versions"]
        ]
    },
    {
        "file": "igetmorechoices",
        "title": "IGetMoreChoices",
        "min_ios": "13.0",
        "tintColor": "orange",
        "screenshots": True,
        "link_source_code": True,
        "description": "<p>Allows for more than 4 choices for Quiz sticker in Instagram.</p>"
    },
    {
        "file": "lpmenabler",
        "title": "LPM Enabler",
        "min_ios": "9.0",
        "max_ios": "14.8.1",
        "tintColor": "yellow",
        "strict_range": True,
        "inline_source_code": True,
        "description": "<p>Natively enables Low Power Mode on your iPod and iPad. You can add Lower Power Mode module to Control Center and you can toggle it from inside Battery settings. You absolutely don't need this tweak for your iPhone or any devices running iOS 15 and above.</p>"
    },
    {
        "file": "batteryhealthenabler",
        "title": "Battery Health Enabler",
        "min_ios": "11.3",
        "featured_as_banner": True,
        "description": "<p>Natively enables Battery Health feature on your iPod and iPad, though the only use case is to see the current maximum capacity of your battery. Nothing else works on non-iPhone technically.</p>"
    },
    {
        "file": "cahighfps",
        "title": "CAHighFPS",
        "min_ios": "7.0",
        "description": "<p>Makes CoreAnimation apps use the highest available FPS (same as your device's refresh rate).\
            Head to Settings > CAHighFPS and enable the tweak for each of your apps. Read <a target=\"_blank\" href=\"https://github.com/PoomSmart/CAHighFPS\">here</a> for how the tweak works under-the-hood.\
            Tested on these apps:</p>",
        "extra_content": "<ol>\
            <li>Asphalt 8/9 (1.1.0+)</li>\
            <li>Safari Browser (1.0.3+)</li>\
            <li>Where's My Water 2</li>\
            <li>Plants vs Zombies (HD)</li>\
            <li>Plants vs Zombies 2</li>\
            <li>Bejeweled Blitz</li>\
            <li>Bejeweled Classic (HD)</li>\
            <li>Bloons TD 5</li>\
            <li>Tiny Wings</li>\
            <li>Real Racing 3</li>\
            <li>Jelly Defense</li>\
        </ol>",
        "changes": [
            ["1.3.3", [
                "Fixed preference not working",
                "Disabled this tweak on SpringBoard"
            ]],
            ["1.3.2", "Removed debug logging"],
            ["1.3.1", "(Rootless-only) Fixed preference not working"],
            ["1.3.0", "Reworked support for Metal apps"],
            ["1.1.2", "Added iOS 15 support"],
            ["1.1.0", [
                    "Added support for an array of Metal-based apps",
                    "Separate system and user apps in sections"
                ]
            ]
        ]
    },
    {
        "file": "injectionfoundation",
        "title": "Injection Foundation",
        "min_ios": "7.0",
        "description": "<p>Injects UIKit tweaks into Foundation apps. Check out the source code for how it works and the motivation behinds on <a target=\"_blank\" href=\"https://github.com/PoomSmart/Injection-Foundation\">GitHub</a>.</p>",
        "changes": [
            ["1.0.1", "Support rootless jailbreaks"]
        ]
    },
    {
        "file": "replaykitmax",
        "title": "ReplayKit Max",
        "min_ios": "9.0",
        "description": "<p>Removes screen recording resolution cap (1600x1600 or 1920x1920) from ReplayKit-based applications, including SpringBoard.</p>\
            <p>Tweak version of <code>defaults write replayd RPFullResCapture -bool 1</code></p>"
    },
    {
        "file": "advancedmapenabler",
        "title": "Advanced Map Enabler",
        "min_ios": "15.0",
        "description": "<p>Enables Advanced Map (3D globe) on unsupported iPhones/iPods/iPads running iOS 15+.</p>"
    },
    {
        "file": "latesttranslate",
        "title": "LatestTranslate",
        "min_ios": "14.0",
        "max_ios": "16.7.15",
        "description": "<p>Makes Apple's Translate app support all languages to date. For example, making all iOS 17 languages available to iOS 15 and 16. If the tweak doesn't work, restart Translate app and ensure you have internet connection. If to no avail, you may reinstall this tweak.</p>",
        "changes": [
            ["6.0.1", "Added new languages from iOS 17"]
        ]
    },
    {
        "file": "osanalytics",
        "title": "OSAnalytics",
        "min_ios": "13.0",
        "description": "<p>Enables the private com.apple.OSAnalytics diagnostics entitlement so that the crash logs will include application-specific system logs whenever applicable. This is very useful for the developers to debug why their tweaks really crash on their consumer devices by looking at the crash logs that are more informative. This package has been uploaded to this repository with the permission of the original author dlevi309.<br /><a target=\"_blank\" href=\"https://github.com/PoomSmart/OSAnalytics\">Source code</a></p>",
        "changes": [
            ["0.0.4", "Added support for iOS 13"],
            ["0.0.3", "Fixed crash in some processes"],
            ["0.0.2", "Properly added support for iOS 15 (credits to @NightwindDev)"]
        ]
    },
    {
        "file": "sfsymbols",
        "title": "SFSymbols",
        "min_ios": "13.0",
        "max_ios": "17.7.5",
        "description": "<p>Backports latest SF Symbols to your device.</p><br/>\
            <p>For developers who want to benefit from the latest SF Symbols in their app, include <code>com.ps.sfsymbols</code> in your control file.</p><br/>\
            <p>There are two SFSymbols packages that have to be used together:</p>",
        "extra_content": "<ol>\
            <li><b>SFSymbols</b>: Makes the system uses SF Symbols from SFSymbolAssets package</li>\
            <li><b>SFSymbolsAssets</b>: Contains the actual SF Symbols assets, will be updated when the newer version came out (usually with iOS update)</li>\
        </ol>",
        "changes": [
            ["1.0.10", "Improved icon compatibility on iOS 15"],
            ["1.0.8", "Fixed potential crash on iOS 15"],
            ["1.0.7", "Improved icon compatibility on iOS 15"],
            ["1.0.3", "Fixed the tweak not working on iOS 17+"],
            ["1.0.2", "Fixed a possible crash on iOS 15"],
            ["1.0.1", "Improved icon compatibility on iOS 15"]
        ]
    },
    {
        "file": "noswiftatruntime",
        "title": "NoSwiftAtRuntime",
        "min_ios": "13.0",
        "max_ios": "16.7.12",
        "description": "<p>Avoids crashing when performing runtime instrumentation on apps with incompatible Swift classes (using recent Swift compiler versions).</p>\
            <p>You can go to Settings > NoSwiftAtRuntime to enable the tweak per app.</p>\
            <p>Reference: <a target=\"_blank\" href=\"https://github.com/swiftlang/swift/issues/72657\">Swift issue #72657</a></p>",
        "changes": [
            ["1.0.2", "Fixed crashing to safe mode for some rootless devices"],
            ["1.0.1", "Allows installation on iOS 16"]
        ]
    }
] + youtube + emoji + camera + springboard + app

sileo_keys = [
    "headerImage", "tintColor", "backgroundColor"
]

def generate_depictions(entries=None):
    generated_count = 0
    for entry in tweaks if entries is None else entries:
        validate_entry(entry)
        file = entry.get("file")
        title = entry.get("title")
        min_ios = entry.get("min_ios")
        max_ios = entry.get("max_ios")
        strict_range = entry.get("strict_range")
        screenshots = entry.get("screenshots")
        featured_as_banner = entry.get("featured_as_banner")
        changes = entry.get("changes")
        # link_source_code = entry.get("link_source_code")
        inline_source_code = entry.get("inline_source_code")
        debug = entry.get("debug")
        description = normalize_markup(entry.get("description"))
        extra_content = entry.get("extra_content")
        if extra_content:
            extra_content = normalize_markup(extra_content)
        output_path = depictions_dir / f"{file}.html"

        source_code = None
        screenshot_objects = collect_screenshots(file) if screenshots else []

        if inline_source_code:
            source_code = load_inline_source_code(file, title)
            if source_code is None:
                continue
        output_path.write_text(minify_html.minify(html_template.render(
                title=title,
                min_ios=min_ios,
                max_ios=max_ios,
                strict_range=strict_range,
                changes=changes,
                screenshots=screenshot_objects,
                description=description,
                extra_content=extra_content,
                source_code=html.escape(source_code) if source_code is not None else None,
                debug=debug
            ), minify_js=False, minify_css=False), encoding="utf-8")
        print(f"Generated {output_path}")
        generated_count += 1

        no_sileo = entry.get("no_sileo")
        if no_sileo:
            continue
        sileo_output_path = sileo_depictions_dir / f"{file}.json"

        with (templates_dir / "index.json").open(encoding="utf-8") as json_file:
            data = json.load(json_file)
            for key in sileo_keys:
                val = entry.get(key)
                if val:
                    data[key] = val
            if featured_as_banner and 'headerImage' not in entry:
                data['headerImage'] = f"https://poomsmart.github.io/repo/features/{file}.png"
            tabs = data["tabs"]
            views = None
            for json_entry in tabs:
                tabname = json_entry["tabname"]
                if tabname == "Details":
                    views = json_entry["views"]
                    views[0]["markdown"] = description
                    if screenshot_objects:
                        screenshots_json = {
                            "class": "DepictionScreenshotsView",
                            "itemCornerRadius": 14,
                            "screenshots": screenshot_objects,
                            "itemSize": "{160,284}"
                        }
                        views.insert(0, screenshots_json)
                    if extra_content:
                        views.append({
                            "class": "DepictionMarkdownView",
                            "markdown": extra_content,
                            "useSpacing": True,
                            "useRawFormat": True
                        })
            if views and min_ios:
                support_versions = {
                    "class": "DepictionSubheaderView",
                    "useMargins": True,
                    "title": f"Compatible with iOS {min_ios} to {max_ios}" if min_ios and max_ios else f"Compatible with iOS {min_ios} +"
                }
                views.insert(0, support_versions)
            if source_code:
                source_code_tab = {
                    "class": "DepictionStackView",
                    "tabname": "Source Code",
                    "views": [
                        {
                            "class": "DepictionMarkdownView",
                            "markdown": f"```\n{source_code}\n```"
                        }
                    ]
                }
                tabs.append(source_code_tab)
            if changes:
                changes_tab = {
                    "class": "DepictionStackView",
                    "tabname": "Changelog",
                    "views": []
                }
                views = changes_tab["views"]
                first_change = True
                for change in changes:
                    if not first_change:
                        views.append({
                            "class": "DepictionSeparatorView"
                        })

                    views.append({
                        "class": "DepictionSubheaderView",
                        "title": f"Version {change[0]}"
                    })
                    change_part = ""
                    if isinstance(change[1], list):
                        for item in change[1]:
                            change_part += f"- {item}\n"
                    else:
                        change_part = f"- {change[1]}"
                    views.append({
                        "class": "DepictionMarkdownView",
                        "markdown": change_part
                    })
                    first_change = False
                tabs.append(changes_tab)

        with sileo_output_path.open('w', encoding="utf-8") as out_file:
            json.dump(data, out_file)
        print(f"Generated {sileo_output_path}")

    return generated_count


def main():
    generate_depictions()


if __name__ == "__main__":
    main()
