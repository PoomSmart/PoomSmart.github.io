# pip3 install jinja2 --user
from jinja2 import Environment, FileSystemLoader
import os, re, json

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
screenshots_dir = os.path.join(root, 'screenshots')
env = Environment(loader=FileSystemLoader(templates_dir), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('index.html')

tweaks = [
    {
        "file": "60fps",
        "title": "60fps",
        "min_ios": "7.0",
        "description": "<p>720p60 for iPhone 4s (H4), 1080p60 and WIP 4k30 for iPhone 5s (H6) and WIP 4kp60 for iPhone SE (1st generation) (H9)</p>",
        "changes": [
            [ "1.0.0~b1", "Compiled with the latest SDK" ]
        ]
    },
    {
        "file": "capture",
        "title": "Capture",
        "min_ios": "8.0",
        "max_ios": "10.3.4",
        "description": "<p>This tweak was fully tested on iPhone 4s iOS 9.0.2/9.3.5. Other devices might support, but is not guaranteed.</p>\
                    <p>This tweak allows you to use Dictation to say words like \"Capture\", \"Cheese\" in order to take photos. You\
                    can personalize words from settings too. One downside of this tweak is that it will not work with devices\
                    with camera using multiple inputs at a time. For instance, iPhone that is compatible with Live Photo\
                    will not support. It was supposed to be the first commercial tweak but the developer itself did basically\
                    give up developing and just opened source this tweak. Perhaps some talented guys out there would refine\
                    it to be something special.</p>"
    },
    {
        "file": "emojiattributes",
        "title": "EmojiAttributes",
        "min_ios": "5.1",
        "changes": [
            [ "1.4.4~b5", "Improved emoji sizing fix logic for iOS 6 - 9" ]
        ],
        "description": "<p>Various under-the-hood fixes for emoji display. See <a href=\"https://github.com/PoomSmart/EmojiAttributes/blob/master/README.md\">here</a> for more information.</p>"
    },
    {
        "file": "emojifontmanager",
        "title": "EmojiFontManager",
        "min_ios": "6.0",
        "changes": [
            [ "1.0.0", "Reworked Settings page for better visual in recent iOS versions" ],
            [ "0.0.8.5", "Use ARC in preference bundle, fixing iOS 7 support" ],
            [ "0.0.8.4", "Use com.apple.UIKit defaults instead of Cephei preferences to overcome sandbox issue" ]
        ],
        "description": "<p><b>**EmojiPort needs to be installed if you also want new emojis.**</b> This tweak allows you to override system's emoji font without swapping them. Access <b>Settings app &gt; EmojFontManager</b>\
                        to choose your font. Fonts (folder with extension .font AND having AppleColorEmoji@2x.ttf/.ttc font inside)\
                        that can be used by this tweak should be placed in <code>/Library/Themes/EmojiFontManager</code>. It is highly recommended\
                        to respring after you change the font.</p>"
    },
    {
        "file": "emojilayout",
        "title": "EmojiLayout",
        "min_ios": "5.1",
        "max_ios": "8.2",
        "strict_range": True,
        "no_sileo": True,
        "changes": [
            [ "1.1.21", "Recognizes iPad emoji landscape keyboard variant" ],
            [ "1.1.20", "Reenabled iOS 5.1 support" ]
        ],
        "description": "<p>Layout emoji keyboard. Specifically, set number of rows and columns of emoji display.</p>"
    },
    {
        "file": "emojilibrary",
        "title": "EmojiLibrary",
        "min_ios": "5.1",
        "changes": [
            [ "1.2.3", "Release version" ]
        ],
        "description": "<p>EmojiLibrary is a developer library, and the master library for most of PoomSmart's Emoji tweaks, including\
                    algorithms and functionalities that handle any kind of emojis - display as images properly. Developers\
                    that want to create emoji-related tweaks would find this useful.</p>"
    },
    {
        "file": "emojiport_5_1",
        "title": "EmojiPort (iOS 5.1)",
        "min_ios": "5.1",
        "max_ios": "5.1.1",
        "strict_range": True,
        "no_sileo": True,
        "changes": [
            [ "1.0.10", "Adopted fixes related to emoji split keyboard from EmojiPort (iOS 6.0-8.2)" ]
        ],
        "description": "<p>Latest emojis for iOS 5.1</p>\
            <p>This EmojiPort variant ports some of the iOS 6 variant for best compatibility on iOS 5. The manual way is recommended, as written in <a href=\"https://poomsmart.github.io/repo/emoji10.html\">here</a>.</p>"
    },
    {
        "file": "emojiport_6",
        "title": "EmojiPort (iOS 6.0 - 8.2)",
        "min_ios": "6.0",
        "max_ios": "8.2",
        "strict_range": True,
        "no_sileo": True,
        "changes": [
            [ "1.7.5", "Fixed crashing when selecting skinned emojis" ]
        ],
        "description": "<p>Latest emojis for iOS 6.0 - 8.2</p>\
                <p><a href=\"https://poomsmart.github.io/repo/emoji10.html\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojiport_8_3",
        "title": "EmojiPort (iOS 8.3 - 8.4)",
        "min_ios": "8.3",
        "max_ios": "8.4.1",
        "strict_range": True,
        "no_sileo": True,
        "changes": [
            [ "1.6.5", "Fixed emoji category icons not being the latest" ]
        ],
        "description": "<p>Latest emojis for iOS 8.3 - 8.4</p>\
                <p><a href=\"https://poomsmart.github.io/repo/emoji10.html\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojiport_9",
        "title": "EmojiPort (iOS 9.0 - 9.3)",
        "min_ios": "9.0",
        "max_ios": "9.3.6",
        "strict_range": True,
        "no_sileo": True,
        "changes": [
            [ "1.6.5", "Fixed emoji category icons not being the latest (iOS 9.0)" ]
        ],
        "description": "<p>Latest emojis for iOS 9.0 - 9.3</p>\
            <p><a href=\"https://poomsmart.github.io/repo/emoji10.html\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojiport_10",
        "title": "EmojiPort (iOS 10.0 - 11.4)",
        "min_ios": "10.0",
        "max_ios": "11.4.1",
        "strict_range": True,
        "changes": [
            [ "1.3.4", "Fixed crashing when using normal skinned emojis" ]
        ],
        "description": "<p>Latest emojis for iOS 10.0 - 11.4</p>\
            <p><a href=\"https://poomsmart.github.io/repo/emoji10.html\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojiport_12",
        "title": "EmojiPort (iOS 12.0 - 14.4)",
        "min_ios": "12.0",
        "max_ios": "14.4.2",
        "strict_range": True,
        "changes": [
            [ "1.1.1", "Release version" ]
        ],
        "description": "<p>Latest emojis for iOS 12.0 - 14.4</p>\
            <p><a href=\"https://poomsmart.github.io/repo/emoji10.html\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "letmeblock",
        "title": "LetMeBlock",
        "min_ios": "9.0",
        "changes": [
            [ "0.0.7.8", "Auto-kill mDNSResponderHelper when mDNSResponder keeps crashing" ],
            [ "0.0.7.5", "Compiled with ARC to support devices with libhooker (Credits to @Diatrus)" ]
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
        "file": "amber",
        "title": "Amber",
        "min_ios": "7.0",
        "tintColor": "orange",
        "changes": [
            [ "0.0.5.1", "Fixed crashing when swiping in expanded flashlight view in Control Center for iOS 13-" ]
        ],
        "description": "<p>A CC module/Flipswitch tweak to allow setting of Amber LED, or both White and Amber LEDs.</p>"
    },
    {
        "file": "quadhighcurrent",
        "title": "QuadHighCurrent",
        "min_ios": "10.0",
        "changes": [
            [ "0.0.4", "Fixed potential crashing on H11ISP and newer camera devices" ]
        ],
        "description": "<p>A CC module/Flipswitch tweak (similar to Amber) to always have the maximum LEDs brightness (i.e., using high current) for quad-LEDs devices. An example is when you turn on the light in video recording mode of the stock camera app. For iPhone 7 and newer, iPad Pro 12.9\" (2nd Gen) and newer.</p>"
    },
    {
        "file": "libsubstitrate",
        "title": "libSubstitrate",
        "min_ios": "5.0",
        "changes": [
            [ "0.0.1-3", "Crash fix for Substrate users" ]
        ],
        "description": "<p>This is a compatibility library for runtime modification tweaks via Substitute and CydiaSubstrate.</p>\
            <p>The motivation of this project is the lack of Substrate support on A12/arm64e for those using Chimera. As Substitute API usually works better on this environment, libSubstitrate will, if available, try to use Substitute API first. Otherwise, it will fall back to Cydia Substrate.</p>"
    },
    {
        "file": "pad56",
        "title": "Pad56",
        "min_ios": "7.0",
        "max_ios": "13.7",
        "description": "<p>5x6 icon layout for iPad and iPad Pro. That's it.</p>"
    },
    {
        "file": "splitit",
        "title": "SplitIt",
        "min_ios": "10.0",
        "changes": [
            [ "0.0.2", "Deprecated libSubstitrate" ]
        ],
        "description": "<p>Enable keyboard split feature on borderless iPads.</p>"
    },
    {
        "file": "pencilpro",
        "title": "Pencil Pro",
        "min_ios": "9.0",
        "changes": [
            [ "0.0.2.5", "Improved iOS 14 support" ]
        ],
        "description": "<p>A little better Apple Pencil functionalities, even though most of the aimed features are somewhat broken.</p>"
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
        "description": "<p>Default size of Animoji/Memoji stickers is no more than 500px * 500px and the stickers look too pixellated. This tweak will simply double the size.</p>"
    },
    {
        "file": "ytuhd",
        "title": "YTUHD SW",
        "min_ios": "11.0",
        "description": "<p>Unlock 1440p and 2160p resolutions in iOS YouTube app.</p>",
        "changes": [
            [ "0.0.3.7", "Hook more methods (by SarahH12099)" ]
        ]
    },
    {
        "file": "youpip",
        "title": "YouPIP",
        "min_ios": "10.0",
        "description": "<p>Enable native PiP in YouTube app.</p>",
        "changes": [
            [ "1.1.0",
                [
                    "Made PiP activated the first time the app is dismissed (iOS 14+)",
                    "Made PiP activated only when the app is dismissed (iOS 13-)"
                ]
            ],
            [ "1.0.0", "Implemented PiP backward-compatible with iOS 13-" ],
            [ "0.0.13", "Fixed crashing when casting a video" ],
            [ "0.0.11", "Activate PiP simply by playing the video and dismissing the app (@lgariv)" ],
            [ "0.0.9", "Support YouTube version 16.17" ],
            [ "0.0.8", "Experimental support for YouTube version 15.47" ]
        ]
    },
    {
        "file": "anywherewidgetsforipad",
        "title": "Anywhere Widgets for iPad",
        "min_ios": "14.0",
        "description": "\
                <p>Allow widgets to be on home screen on iPad.</p>\
                <p>Also adjusts the home screen icon grid size to 8x6 (or 7x5 zoomed) to compromise the differences in icon size categories.</p>",
        "changes": [
            [ "1.3.0", "Fixed widgets being off grid at the edge and Added one more row for Portrait grid" ]
        ]
    },
    {
        "file": "apppad",
        "title": "AppPad",
        "min_ios": "9.0",
        "description": "<p>Full screen, Split and Slideover for every app on iPad.</p>",
        "changes": [
            [ "1.0.0", "Use AltList for listing applications" ],
            [ "0.0.2", "You can now configure blacklisted applications from Settings" ]
        ]
    },
    {
        "file": "applibraryforipad",
        "title": "App Library for iPad",
        "min_ios": "14.0",
        "description": "\
                <p>Enable App Library on iPad.</p>\
                <p>Known issue: App Library in Landscape orientation is not maximized.</p>",
        "changes": [
            [ "1.0.1", "Fixed homescreen widgets in sidebar not appearing right after respring" ],
            [ "1.0.0", "Initial release" ]
        ]
    },
    {
        "file": "ytclassicvideoquality",
        "title": "YTClassicVideoQuality",
        "min_ios": "11.0",
        "description": "<p>Revert to the original video quality selector in YouTube app.</p>",
        "changes": [
            [ "1.0.1", "Fixed crashing in YouTube 16.20.5" ],
            [ "1.0.0", "Initial release" ]
        ]
    },
    {
        "file": "igclassiclayout",
        "title": "IGClassicLayout",
        "min_ios": "13.0",
        "screenshots": True,
        "description": "<p>Restore the original buttons layout in Instagram; Home-Reels-Compose-Likes-Profile at bottom and Search-Messages at top.</p>",
        "changes": [
            [ "1.0.0", "Initial release" ]
        ]
    },
]

sileo_keys = [
    "headerImage", "tintColor"
]

for entry in tweaks:
    file = entry.get("file")
    title = entry.get("title")
    min_ios = entry.get("min_ios")
    max_ios = entry.get("max_ios")
    strict_range = entry.get("strict_range")
    screenshots = entry.get("screenshots")
    changes = entry.get("changes")
    debug = entry.get("debug")
    description = re.sub(r'\s+', ' ', entry.get("description"))
    output_path = os.path.join(root, "depictions", "%s.html" % file)

    screenshot_objects = list(map(
        lambda e: {
            "url": "https://poomsmart.github.io/repo/screenshots/%s/%s" % (file, e.name),
            "accessibilityText": e.name
        },
        os.scandir(os.path.join(screenshots_dir, file))
    )) if screenshots else None

    with open(output_path, 'w') as fh:
        fh.write(template.render(
            title=title,
            min_ios=min_ios,
            max_ios=max_ios,
            strict_range=strict_range,
            changes=changes,
            screenshots=screenshot_objects,
            description=description,
            debug=debug
        ))
    print("Generated %s" % output_path)

    no_sileo = entry.get("no_sileo")
    if no_sileo:
        continue
    sileo_output_path = os.path.join(root, "sileodepictions", "%s.json" % file)
   
    with open(os.path.join(templates_dir, "sileo.json")) as json_file:  
        data = json.load(json_file)
        for key in sileo_keys:
            val = entry.get(key)
            if val:
                data[key] = val
        tabs = data["tabs"]
        for json_entry in tabs:
            tabname = json_entry["tabname"]
            if tabname == "Details":
                views = json_entry["views"]
                views[0]["markdown"] = description
                views[2]["text"] = "PoomSmart"
                if screenshot_objects is not None and screenshot_objects.count:
                    screenshots_json = {
                        "class": "DepictionScreenshotsView",
                        "itemCornerRadius": 14,
                        "screenshots": screenshot_objects,
                        "itemSize": "{160,284}"
                    }
                    views.insert(0, screenshots_json)
        if min_ios:
            support_versions = {
                "class": "DepictionSubheaderView",
                "useMargins": True,
                "title": "Compatible with iOS %s to %s" % (min_ios, max_ios) if min_ios and max_ios else "Compatible with iOS %s +" % min_ios
            }
            views.insert(0, support_versions)
        if changes:
            changes_tab = {
                "class": "DepictionStackView",
                "tabname": "Latest Changes",
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
                    "title": "Version %s" % change[0]
                })
                change_part = ""
                if isinstance(change[1], list):
                    for c in change[1]:
                        change_part += "- %s\n" % c
                else:
                    change_part = "- %s" % change[1]
                views.append({
                    "class": "DepictionMarkdownView",
                    "markdown": change_part
                })
                first_change = False
            tabs.append(changes_tab)

    with open(sileo_output_path, 'w') as out_file:
        json.dump(data, out_file)
    print("Generated %s" % sileo_output_path)
