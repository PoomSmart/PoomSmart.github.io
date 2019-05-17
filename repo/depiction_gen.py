from jinja2 import Environment, FileSystemLoader
import os, re, json

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment(loader=FileSystemLoader(templates_dir), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('index.html')

tweaks = [
    {
        "file": "test",
        "title": "Test",
        "min_ios": "6.0",
        "max_ios": "12.1",
        "strict_range": True,
        "description": "<p>Test package <a href=\"#\">with some URL</a></p>\
            <li>\
                <p>Option 1</p>\
                <p>Option 2</p>\
                <p>Option 3</p>\
            </li>",
        "changes": [
            [ "0.0.2", "Sileo Depiction WIP" ]
        ],
        "debug": True
    },
    {
        "file": "60fps",
        "title": "60fps",
        "min_ios": "7.0",
        "description": "<p>720p60 for iPhone 4s (H4 Cameras) and 1080p60 for iPhone 5s (H6 Cameras excluding A9 devices)</p>"
    },
    {
        "file": "capture",
        "title": "Capture",
        "min_ios": "8.0",
        "max_ios": "10.3.3",
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
        "max_ios": "12.0.9",
        "changes": [
            [ "1.3.21", "Attempt to fix crash" ],
            [ "1.3.20", "Trying libSubstitrate" ],
            [ "1.3.19", "arm64e" ]
        ],
        "description": "<p>Various under-the-hood fixes for emoji display. See <a href=\"https://github.com/PoomSmart/EmojiAttributes/blob/master/README.md\">here</a> for more information.</p>"
    },
    {
        "file": "emojifontmanager",
        "title": "EmojiFontManager",
        "min_ios": "6.0",
        "description": "<p>This tweak allows you to override system's emoji font without swapping them. Access Settings app &gt; EmojFontManager\
                        to choose your font. Fonts (folder with extension .font AND having AppleColorEmoji@2x.ttf/.ttc font inside)\
                        that can be used by this tweak should be placed in /Library/Themes/EmojiFontManager. It is highly recommended\
                        to respring after you change the font.</p>"
    },
    {
        "file": "emojilayout",
        "title": "EmojiLayout",
        "min_ios": "5.1",
        "max_ios": "8.2",
        "strict_range": True,
        "no_sileo": True,
        "description": "<p>Layout emoji keyboard. Specifically, set number of rows and columns of emoji display.</p>",
    },
    {
        "file": "emojilibrary",
        "title": "EmojiLibrary",
        "min_ios": "5.1",
        "changes": [
            [ "1.0.18.1", "Fix iOS 7 support due to Xcode 10.2" ]
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
        "description": "<p>Latest emojis for iOS 8.3 - 8.4</p>\
                <p><a href=\"https://poomsmart.github.io/repo/emoji10.html\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojiport_9",
        "title": "EmojiPort (iOS 9.0 - 9.3)",
        "min_ios": "9.0",
        "max_ios": "9.3.5",
        "strict_range": True,
        "no_sileo": True,
        "description": "<p>Latest emojis for iOS 9.0 - 9.3</p>\
            <p><a href=\"https://poomsmart.github.io/repo/emoji10.html\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojiport_10",
        "title": "EmojiPort (iOS 10.0 - 11.4)",
        "min_ios": "10.0",
        "max_ios": "11.4.1",
        "strict_range": True,
        "description": "<p>Latest emojis for iOS 10.0 - 11.4</p>\
            <p><a href=\"https://poomsmart.github.io/repo/emoji10.html\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojiport_12",
        "title": "EmojiPort (iOS 12.0)",
        "min_ios": "12.0",
        "max_ios": "12.0.9",
        "strict_range": True,
        "changes": [
            [ "1.0.2", "arm64e" ]
        ],
        "description": "<p>Latest emojis for iOS 12.0</p>\
            <p><a href=\"https://poomsmart.github.io/repo/emoji10.html\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "letmeblock",
        "title": "LetMeBlock",
        "min_ios": "9.0",
        "changes": [
            [ "0.0.6.7", "Better memory limit unlocking technique" ],
            [ "0.0.6.6-2", "libSubstitrate 0.0.1-2" ],
            [ "0.0.6.6", "Requires libSubstitrate" ],
            [ "0.0.6.5", "arm64e" ]
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
        "file": "quadhighcurrent",
        "title": "QuadHighCurrent",
        "min_ios": "10.0",
        "description": "<p>A CC module/Flipswitch tweak (similar to Amber) to always have the maximum LEDs brightness (i.e., using high current) for quad-LEDs devices. An example is when you turn on the light in video recording mode of the stock camera app. For iPhone 7 and newer, iPad Pro 12.9\" (2nd Gen) and newer.</p>"
    },
    {
        "file": "silactions",
        "title": "Silactions",
        "min_ios": "11.0",
        "changes": [
            [ "1.0.4", "Bug fixes and improvement" ],
            [ "1.0.3", "Supports Sileo 1.0.7" ],
            [ "1.0.2", "Supports Sileo 1.0.6" ],
            [ "1.0.1", "Cancel button added" ]
        ],
        "description": "<p>Manage packages in Sileo easier. Right now, it can:</p>\
            <li>\
                <p>- Pressing the complete button that is shown after package (un)installation will dismiss the window so you can install other packages (DismissProgress-like)</p>\
                <p>- Tap and Hold the complete button to invoke its original action</p>\
                <p>- Tap and Hold a package cell to review actions (SwipeForMore-like)</p>\
            </li>"
    },
    {
        "file": "libsubstitrate",
        "title": "libSubstitrate",
        "min_ios": "5.0",
        "changes": [
            [ "0.0.1-3", "Crash fix for Substrate users" ],
            [ "0.0.1-2", "Function labels changed" ]
        ],
        "description": "<p>This is a compatibility library for runtime modification tweaks via Substitute and Cydia Substrate.</p>\
            <p>The motivation of this project is the lack of Substrate support on A12/arm64e for those using Chimera. As Substitute API usually works better on this environment, libSubstitrate will, if available, try to use Substitute API first. Otherwise, it will fall back to Cydia Substrate.</p>"
    }
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
    changes = entry.get("changes")
    debug = entry.get("debug")
    description = re.sub(r'\s+', ' ', entry.get("description"))
    output_path = os.path.join(root, "depictions", "%s.html" % file)
    with open(output_path, 'w') as fh:
        fh.write(template.render(
            title=title,
            min_ios=min_ios,
            max_ios=max_ios,
            strict_range=strict_range,
            changes=changes,
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
        if min_ios:
            support_versions = {
                "class": "DepictionSubheaderView",
                "useMargins": True,
                "title": "Compatiable with iOS %s to %s" % (min_ios, max_ios) if min_ios and max_ios else "Compatible with iOS %s +" % min_ios
            }
            views.insert(0, support_versions)
        if changes:
            changes_tab = {
                "tabname": "Latest Changes",
                "views": [],
                "class": "DepictionStackView"
            }
            views = changes_tab["views"]
            for change in changes:
                views.append({
                    "class": "DepictionSubheaderView",
                    "title": "Version %s" % change[0]
                })
                change_part = ""
                if isinstance(change[1], list):
                    for c in change[1]:
                        change_part += "<li>%s</li>" % c
                    change_part = "<ul>%s</ul>" % change_part
                else:
                    change_part = "<ul><li>%s</li></ul>" % change[1]
                views.append({
                    "markdown": change_part,
                    "useRawFormat": True,
                    "class": "DepictionMarkdownView"
                })
                views.append({
                    "class": "DepictionSeparatorView"
                })
            tabs.append(changes_tab)

    with open(sileo_output_path, 'w') as out_file:
        json.dump(data, out_file)
    print("Generated %s" % sileo_output_path)
