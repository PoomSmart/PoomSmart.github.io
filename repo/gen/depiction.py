# follow https://rustup.rs
# pip3 install maturin jinja2 minify-html
import html
import json
import os
import re
import minify_html
from jinja2 import Environment, FileSystemLoader
from youtube import *
from emoji import *
from camera import *

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, '../templates')
screenshots_dir = os.path.join(root, '../screenshots')
env = Environment(loader=FileSystemLoader(templates_dir), trim_blocks=True, lstrip_blocks=True)
html_template = env.get_template('index.html')

tweaks = [
    {
        "file": "letmeblock",
        "title": "LetMeBlock",
        "min_ios": "9.0",
        "changes": [
            ["1.2.1", "Fixed mDNSResponderHelper not being spawn on modern iOS versions so that the memory limit can be lifted for mDNSResponder"],
            ["1.2.0", "(Rootless) Added libSandy profile to allow access to /var/jb/etc/hosts"],
            ["1.1.0", "Added support for rootless jailbreaks (/var/jb/etc/hosts)"],
            ["1.0.0", "Increased Jetsam memory limit to 512 MB"]
        ],
        "description": "<p><a href=\"https://github.com/PoomSmart/LetMeBlock/blob/master/README.md\">README</a></p>"
    },
    {
        "file": "smoothkb",
        "title": "SmoothKB",
        "min_ios": "7.0",
        "description": "<p>Fade animation across keyboard typing.</p>"
    },
    {
        "file": "libsubstitrate",
        "title": "libSubstitrate",
        "min_ios": "5.0",
        "changes": [
            ["0.0.1-3", "Crash fix for Substrate users"]
        ],
        "description": "<p>This is a compatibility library for runtime modification tweaks via Substitute and CydiaSubstrate.</p>\
            <p>The motivation of this project is the lack of Substrate support on A12/arm64e for those using Chimera. As Substitute API usually works better on this environment, libSubstitrate will, if available, try to use Substitute API first. Otherwise, it will fall back to Cydia Substrate.</p>"
    },
    {
        "file": "padgrid",
        "title": "PadGrid",
        "min_ios": "7.0",
        "description": "<p>Increase home screen icon grid size for iPad.</p>",
        "changes": [
            ["1.2.0", "Added Reduce edge insets option for iPadOS 15+"],
            ["1.1.2", "Made IconOrder an option for icon layout persistence library"],
            ["1.1.1", "Added folder rows and columns settings (iOS 14+, contributed by @UInt2048)"]
        ]
    },
    {
        "file": "splitit",
        "title": "SplitIt",
        "min_ios": "10.0",
        "max_ios": "13.7",
        "changes": [
            ["0.0.2", "Deprecated libSubstitrate"]
        ],
        "description": "<p>Enable keyboard split feature on borderless iPads.</p>"
    },
    {
        "file": "pencilpro",
        "title": "Pencil Pro",
        "min_ios": "9.0",
        "changes": [
            ["1.0.0", "Fixed issues with GoodNotes 5 app"]
        ],
        "description": "<p>A little better Apple Pencil functionalities, even though most of the aimed features are somewhat broken.</p>\
            <p>For more details, visit tweak's <a href=\"https://github.com/PoomSmart/PencilPro/blob/master/README.md\">README</a>.</p>"
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
        "file": "anywherewidgetsforipad",
        "title": "Anywhere Widgets for iPad",
        "min_ios": "14.0",
        "max_ios": "14.8.1",
        "strict_range": True,
        "featured_as_banner": True,
        "description": "<p>Allow widgets to be on home screen on iPad.</p>",
        "changes": [
            ["1.4.0", "Removed icon grid size overrides, please use PadGrid to adjust this instead"]
        ]
    },
    {
        "file": "apppad",
        "title": "AppPad",
        "min_ios": "9.0",
        "description": "<p>Full screen, Split and Slideover for every app on iPad.</p>",
        "changes": [
            ["1.1.2", "(Rootless-only) Fixed preference not working"],
            ["1.1.1", "Fixed tweak not being injected into SpringBoard sometimes"]
        ]
    },
    {
        "file": "igclassiclayout",
        "title": "IGClassicLayout",
        "min_ios": "13.0",
        "tintColor": "orange",
        "description": "<p>Restore the original-ish buttons layout in Instagram.</p>",
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
        "description": "<p>Allow for more than 4 choices for Quiz sticker in Instagram.</p>"
    },
    {
        "file": "nottodayhomescreensidebar",
        "title": "NotTodayHomeScreenSideBar",
        "min_ios": "14.0",
        "max_ios": "14.8.1",
        "strict_range": True,
        "screenshots": True,
        "featured_as_banner": True,
        "inline_source_code": True,
        "description": "<p>Prevent Today View sidebar from being pinned on iPad homescreen. Widgets in Today View will still be accessible by swiping to the leftmost of the homescreen, just like how it is on iPad portrait or iPhone.</p>"
    },
    {
        "file": "expandedclassicscreen",
        "title": "expandedclassicscreen",
        "min_ios": "14.0",
        "screenshots": True,
        "inline_source_code": True,
        "description": "<p>Use a larger 414x736 (iPhone 6s+) resolution for classic apps on iPad.</p>"
    },
    {
        "file": "lpmenabler",
        "title": "LPM Enabler",
        "min_ios": "11.0",
        "max_ios": "14.8.1",
        "tintColor": "yellow",
        "strict_range": True,
        "inline_source_code": True,
        "description": "<p>Natively enable Low Power Mode on your iPod and iPad. You can add Lower Power Mode module to Control Center and you can toggle it from inside Battery settings. You absolutely don't need this tweak for your iPhone or any devices running iOS 15 and above.</p>"
    },
    {
        "file": "batteryhealthenabler",
        "title": "Battery Health Enabler",
        "min_ios": "11.3",
        "featured_as_banner": True,
        "description": "<p>Natively enable Battery Health feature on your iPod and iPad, though the only use case is to see the current maximum capacity of your battery. Nothing else works on non-iPhone technically.</p>"
    },
    {
        "file": "cconoff",
        "title": "CC On & Off",
        "min_ios": "11.0",
        "description": "<p>Toggle Wi-Fi and Bluetooth On/Off explicitly from Control Center on iOS 11+.</p>",
        "changes": [
            ["1.1.0", "Fixed Bluetooth not turning off on iOS 15"],
            ["1.0.0", "Compiled with ARC"]
        ]
    },
    {
        "file": "cahighfps",
        "title": "CAHighFPS",
        "min_ios": "7.0",
        "description": "<p>Make CoreAnimation apps use the highest available FPS (same as your device's refresh rate).\
            Head to Settings > CAHighFPS and enable the tweak for each of your apps. Read <a href=\"https://github.com/PoomSmart/CAHighFPS\">here</a> for how the tweak works under-the-hood.\
            Tested on these apps:</p>",
        "extra_content": "<ul>\
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
        </ul>",
        "changes": [
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
        "description": "<p>Inject UIKit tweaks into Foundation apps. Check out the source code for how it works and the motivation behinds on <a href=\"https://github.com/PoomSmart/Injection-Foundation\">GitHub</a>.</p>",
        "changes": [
            ["1.0.1", "Support rootless jailbreaks"]
        ]
    },
    {
        "file": "replaykitmax",
        "title": "ReplayKit Max",
        "min_ios": "9.0",
        "description": "<p>Remove screen recording resolution cap (1600x1600 or 1920x1920) from ReplayKit-based applications, including SpringBoard.</p>\
            <p>Tweak version of <code>defaults write replayd RPFullResCapture -bool 1</code></p>"
    },
    {
        "file": "blurrybadges",
        "title": "Blurry Badges",
        "min_ios": "14.0",
        "description": "<p>Add colored blur to SpringBoard icon badges.</p>",
        "changes": [
            ["1.5.2", "Fixed crash on iOS 14"],
            ["1.5.1", [
                "Fixed crash when Continuity apps appear on the home screen",
                "Fixed badge icon of Continuity apps not being displayed"
            ]],
            ["1.5.0", [
                "Significantly improved performance of blurry badges implementation",
                "iOS 16+ support"
            ]],
            ["1.4.3", "iOS 15 support"]
        ]
    },
    {
        "file": "advancedmapenabler",
        "title": "Advanced Map Enabler",
        "min_ios": "15.0",
        "description": "<p>Enable Advanced Map (3D globe) on unsupported iPhones/iPods/iPads running iOS 15+.</p>"
    },
    {
        "file": "latesttranslate",
        "title": "LatestTranslate",
        "min_ios": "14.0",
        "max_ios": "16.7.5",
        "description": "<p>Make Apple's Translate app support all languages to date. For example, making all iOS 17 languages available to iOS 15 and 16. If the tweak doesn't work, restart Translate app and ensure you have internet connection. If to no avail, you may reinstall this tweak.</p>",
        "changes": [
            ["6.0.0", "Added new languages from iOS 17"]
        ]
    },
] + youtube + emoji + camera

sileo_keys = [
    "headerImage", "tintColor", "backgroundColor"
]

for entry in tweaks:
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
    description = re.sub(r'\s+', ' ', entry.get("description"))
    extra_content = entry.get("extra_content")
    if extra_content:
        extra_content = re.sub(r'\s+', ' ', extra_content)
    output_path = os.path.join(root, "../depictions", f"{file}.html")

    SOURCE_CODE = None
    screenshot_objects = list(filter(None, list(map(
        lambda e: None if e.name.startswith('.') else {
            "url": f"https://poomsmart.github.io/repo/screenshots/{file}/{e.name}",
            "accessibilityText": e.name
        },
        os.scandir(os.path.join(screenshots_dir, file))
    )))) if screenshots else None

    if inline_source_code:
        SOURCE_CODE_FOUND = False
        POSSIBLE_FOLDERS = ['SpringBoard-Switch', 'System-iOS', 'YouTube', 'Camera']
        try:
            for folder in POSSIBLE_FOLDERS:
                source_code_path = f'../../{folder}/{file}/Tweak.x'
                if os.path.exists(source_code_path):
                    with open(source_code_path, 'r') as source_code_content:
                        SOURCE_CODE = source_code_content.read()
                        SOURCE_CODE_FOUND = True
                        break
        except IOError:
            print(f"Could not read source code of {title}")
        if not SOURCE_CODE_FOUND:
            print(f"Source code of {title} not found")
            continue
    with open(output_path, 'w') as fh:
        fh.write(minify_html.minify(html_template.render(
            title=title,
            min_ios=min_ios,
            max_ios=max_ios,
            strict_range=strict_range,
            changes=changes,
            screenshots=screenshot_objects,
            description=description,
            extra_content=extra_content,
            source_code=html.escape(SOURCE_CODE) if SOURCE_CODE is not None else None,
            debug=debug
        ), minify_js=False, minify_css=False))
    print(f"Generated {output_path}")

    no_sileo = entry.get("no_sileo")
    if no_sileo:
        continue
    sileo_output_path = os.path.join(root, "../sileodepictions", f"{file}.json")

    with open(os.path.join(templates_dir, "index.json")) as json_file:
        data = json.load(json_file)
        for key in sileo_keys:
            val = entry.get(key)
            if val:
                data[key] = val
        if featured_as_banner and 'headerImage' not in entry:
            data['headerImage'] = f"https://poomsmart.github.io/repo/features/{file}.png"
        tabs = data["tabs"]
        VIEWS = None
        for json_entry in tabs:
            tabname = json_entry["tabname"]
            if tabname == "Details":
                VIEWS = json_entry["views"]
                VIEWS[0]["markdown"] = description
                if screenshot_objects is not None and screenshot_objects.count:
                    screenshots_json = {
                        "class": "DepictionScreenshotsView",
                        "itemCornerRadius": 14,
                        "screenshots": screenshot_objects,
                        "itemSize": "{160,284}"
                    }
                    VIEWS.insert(0, screenshots_json)
                if extra_content:
                    VIEWS.append({
                        "class": "DepictionMarkdownView",
                        "markdown": extra_content,
                        "useSpacing": True,
                        "useRawFormat": True
                    })
        if VIEWS and min_ios:
            support_versions = {
                "class": "DepictionSubheaderView",
                "useMargins": True,
                "title": f"Compatible with iOS {min_ios} to {max_ios}" if min_ios and max_ios else f"Compatible with iOS {min_ios} +"
            }
            VIEWS.insert(0, support_versions)
        if SOURCE_CODE:
            source_code_tab = {
                "class": "DepictionStackView",
                "tabname": "Source Code",
                "views": [
                    {
                        "class": "DepictionMarkdownView",
                        "markdown": f"```\n{SOURCE_CODE}\n```"
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
            VIEWS = changes_tab["views"]
            FIRST_CHANGE = True
            for change in changes:
                if not FIRST_CHANGE:
                    VIEWS.append({
                        "class": "DepictionSeparatorView"
                    })

                VIEWS.append({
                    "class": "DepictionSubheaderView",
                    "title": f"Version {change[0]}"
                })
                CHANGE_PART = ""
                if isinstance(change[1], list):
                    for c in change[1]:
                        CHANGE_PART += f"- {c}\n"
                else:
                    CHANGE_PART = f"- {change[1]}"
                VIEWS.append({
                    "class": "DepictionMarkdownView",
                    "markdown": CHANGE_PART
                })
                FIRST_CHANGE = False
            tabs.append(changes_tab)

    with open(sileo_output_path, 'w') as out_file:
        json.dump(data, out_file)
    print(f"Generated {sileo_output_path}")
