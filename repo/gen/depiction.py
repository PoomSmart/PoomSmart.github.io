# follow https://rustup.rs
import html
import json
import os
import re
import minify_html
from jinja2 import Environment, FileSystemLoader
from youtube import *
from emoji import *
from camera import *
from springboard import *

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
        "max_ios": "16.7.11",
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
        "file": "githubweblegacycompat",
        "title": "GitHubWebLegacyCompat",
        "min_ios": "8.0",
        "max_ios": "16.3.1",
        "description": "<p>Makes GitHub website more accessible on iOS 16.3 and lower by injecting JS and CSS with unsupported syntax removed.</p>",
        "changes": [
            ["2.3.1", "Updated JS for the recent GitHub changes"],
            ["2.3.0", "Fixed remaining layout issues in the issue(s) page on iOS < 15.4"],
            ["2.2.0", [
                "Fixed some broken elements in the issues page on iOS < 15.4",
                "Made the JS code injected only once"
            ]],
            ["2.1.1", "Fixed GitHub website crashing in some pages"],
            ["2.1.0", [
                "Fixed commit description and time not being displayed on iOS < 16.4",
                "Fixed some broken control elements on iOS < 15.4",
                "Minified CSS code before injecting"
            ]],
            ["2.0.0", "Made JS code loaded from files"],
            ["1.0.7", "Made \"Get assets\" button appear for expanded assets as well"],
            ["1.0.6", "Added Polyfills tweak as a dependency"],
            ["1.0.5", [
                "Added \"Get assets\" button to GitHub Releases page on iOS 14 and lower to work around the assets being not downloadable",
                "Allows installation on iOS 8"
            ]],
            ["1.0.4", "Added support for iOS 9 - 11"],
            ["1.0.3", [
                "Added stub value for HTMLDialogElement interface so that GitHub Search feature can work",
                "Added com.apple.WebKit to the tweak plist so that it works on App Store browsers"
            ]],
            ["1.0.2", "Added polyfill for Array.prototype.at so that Issues page can be loaded"],
            ["1.0.1", "Removed unnecessary bits"]
        ]
    },
    {
        "file": "chatgptweblegacycompat",
        "title": "ChatGPTWebLegacyCompat",
        "min_ios": "15.0",
        "max_ios": "15.8.4",
        "description": "<p>Makes ChatGPT website more accessible on iOS 15.0 - 15.8 by injecting CSS with unsupported syntax removed.</p>",
        "changes": [
            ["1.3.1", "Made the JS code injected only once"],
            ["1.3.0", [
                "Fixed the tweak not working on iOS 15.0 - 15.3",
                "Made the CSS code loaded from files"
            ]],
            ["1.2.0", [
                "Depends on Polyfills 1.12.0+",
                "Made the JS code loaded from files",
                "Allows installation on iOS 14, but the functionality is still broken"
            ]],
            ["1.1.0", "Allows installation on iOS 15.4 - 15.8, fixing a small layout bug with the chat input box"]
        ]
    },
    {
        "file": "polyfills",
        "title": "Polyfills",
        "min_ios": "8.0",
        "description": "<p>Provides polyfills for some JavaScript features that are not available on old iOS versions.</p>\
            <p>Check out this <a href=\"https://github.com/PoomSmart/Polyfills/blob/main/WKExperimentalFeatures.md\">page</a> for recommended experimental WebKit features to enable to further enhance web compatibility.</p>\
            <p>Up until 2025, iOS 15 and lower are considered \"old\". A lot of websites would outright stop working on these versions as they no longer provide necessary polyfills.</p>\
            <p>Avoid installing version 1.5.0 to 1.9.0 on iOS 15 and lower as there is a high CPU usage bug.</p>",
        "changes": [
            ["2.2.0", [
                "Made CSS Cascade layers workaround work for dynamically added stylesheets",
                "Added polyfill for EventTarget (< 14.0)",
                "Readded `max-width: 100% and overflow-x: hidden` CSS workaround (< 15.0)",
                "Fixed HTMLDialogElement stub polyfill not working (< 15.4)"
            ]],
            ["2.1.0", [
                "Made the JS code injected as soon as it is loaded from the filesystem",
                "Simplified polyfill for CompressionStream"
            ]],
            ["2.0.0", [
                "Made all JS code loaded from files only when needed by that iOS version to reduce memory footprint on injection",
                "Added polyfills for Array.group, Array.groupBy, Array.groupToMap, Object.groupBy, Map.groupBy and Promise.withResolvers (< 17.4)",
                "Fixed Element.matches compatibility workaround not working on iOS 15.4 - 15.5 (< 15.6)"
            ]],
            ["1.12.0", [
                "Worked around CSS dynamic viewport units not working by replacing `{d,s,l}v{w,h} with just v{w,h} (< 16.4)",
                "Worked around CSS Cascade layers not working by stripping `@layer` from stylesheets (< 15.4)",
                "Prevented HTMLDialogElement stub polyfill from being injected if its corresponding experimental WebKit feature is enabled (< 15.4)"
            ]],
            ["1.11.0", [
                "Added the settings page to enable/disable the tweak",
                "Disabled RegExp lookbehind polyfill on twitter.com to avoid breaking the website (< 16.4)"
            ]],
            ["1.10.0", [
                "Fixed requesting desktop website not working in Safari",
                "Added polyfills for Array.from (< 9.0), Array.fromAsync (< 16.4) and Array.includes (< 9.0)",
                "Added polyfill for CSS.escape (< 10.1)",
                "Added polyfill for NodeList.forEach (< 10.0)",
                "Added polyfills for Object.assign (< 9.0), Object.entries (< 10.1) and Object.values (< 10.1)",
                "Added polyfill for Proxy (< 10.0)",
                "Added polyfills for String.startsWith, String.endsWith and String.includes (< 9.0)",
                "Added polyfill for Symbol.asyncIterator (< 11.1)",
                "Added polyfill for WeakSet (< 9.0)"
            ]],
            ["1.9.2", [
                "Fixed user agent spoofing not working (regression of 1.9.1)",
                "Fixed Safari crashing on iOS 8"
            ]],
            ["1.9.1", [
                "Added polyfill for RegExp lookbehind (< 16.4)",
                "Added polyfill for BroadcastChannel (< 15.4)",
                "Added polyfill for Array.toReversed (< 16.0)",
                "Spoofed iOS version to 16.0",
                "Fixed websites always loading in desktop mode",
                "Fixed polyfill compatibility with iOS 13.0 and lower",
                "Fixed polyfill for Array.at, Array.findLast and Array.findLastIndex",
                "Fixed the same polyfill scripts being injected multiple times",
                "Restricted certain polyfills to execute only on the maximum unsupported iOS version and lower",
                "Restricted CompressionStream polyfill to iOS 16.3 and lower",
                "Restricted ReadableStream, WritableStream and TransformStream polyfills to iOS 14.0 and lower",
                "Restricted WebStreams polyfill to iOS 14.0 and lower"
            ]],
            ["1.4.0", [
                "Added missing polyfill for Web Streams (necessary for CompressionStream)",
                "Added polyfill for Element.checkVisibility (< 17.4)",
                "Removed problematic `max-width: 100% and overflow-x: hidden` CSS workaround"
            ]],
            ["1.3.0", [
                "Allows polyfills to be injected into iframes",
                "Added polyfill for CompressionStream (< 16.4)",
                "Fixed support for old iOS versions"
            ]],
            ["1.2.0", "Added polyfills for Promise.allSettled and the meta viewport min-width"],
            ["1.1.1", "Removed the code that removes all other user scripts"],
            ["1.1.0", [
                "Minified all JavaScript codes before injecting",
                "Added support for injecting JavaScript after the document is loaded",
                "Added polyfills for Array.findLast, Array.findLastIndex and Object.hasOwn (< 15.4)",
                "Added polyfill for String.replaceAll (< 13.1)",
                "Added `max-width: 100% and overflow-x: hidden` CSS workaround for html and body to fix incomplete page width on iOS 14 and lower"
            ]],
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
        "max_ios": "16.7.11",
        "description": "<p>Avoids crashing when performing runtime instrumentation on apps with incompatible Swift classes (using recent Swift compiler versions).</p>\
            <p>You can go to Settings > NoSwiftAtRuntime to enable the tweak per app.</p>\
            <p>Reference: <a target=\"_blank\" href=\"https://github.com/swiftlang/swift/issues/72657\">Swift issue #72657</a></p>",
        "changes": [
            ["1.0.2", "Fixed crashing to safe mode for some rootless devices"],
            ["1.0.1", "Allows installation on iOS 16"]
        ]
    }
] + youtube + emoji + camera + springboard

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
        POSSIBLE_FOLDERS = ['SpringBoard', 'YouTube', 'Camera']
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
