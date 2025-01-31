emoji = [
    {
        "file": "emojiport10resources",
        "title": "EmojiPort Resources (iOS 10+)",
        "min_ios": "10.0",
        "changes": [
            ["1.6.0", "Updated to iOS 17.4 assets"]
        ],
        "description": "<p>Up-to-date emoji assets (bitmap, localization, metadata) specific to iOS 10 and above.</p>"
    },
    {
        "file": "emojiattributes",
        "title": "EmojiAttributes",
        "min_ios": "5.1",
        "changes": [
            ["1.8.3", "Ported the latest changes in CFStringGetRangeOfCharacterClusterAtIndex to iOS < 15"],
            ["1.8.2", "Fixed crash on iOS 6 due to using modern-only libroot"],
            ["1.8.1", "Compiled with the latest Theos revision"],
            ["1.8.0~b2", [
                "Rootless: Simplify hooks for iOS 15.4+ (may require Dopamine 2)",
                "Rootful: Fixed crash on iOS 12 arm64e devices"
                "Initial Unicode 15.1 support"
            ]],
            ["1.7.1", [
                "Rootless: Use alternative libicucore hooks to work around ElleKit issues (REQUIRE ElleKit 0.6+)",
                "Rootful: Optimized hooks"
                "Unicode 15.0 support",
                "Fixed installation issue on readonly filesystems devices",
                "Fixed new emojis displayed as ? on iOS 10 and lower",
                "Use _NSGetExecutablePath to detect process type"
            ]]
        ],
        "description": "<p>Various under-the-hood fixes for emoji display. See <a href=\"https://github.com/PoomSmart/EmojiAttributes/blob/master/README.md\">here</a> for more information.</p>"
    },
    {
        "file": "emojifontmanager",
        "title": "EmojiFontManager",
        "min_ios": "6.0",
        "changes": [
            ["1.3.8", "Fixed crash on iOS 6 due to using modern-only libroot"],
            ["1.3.7", "Sort fonts alphabetically"],
            ["1.3.6", "Removed debug code"],
            ["1.3.5", [
                "Fixed emojis not rendered correctly on iOS 10",
                "Use _NSGetExecutablePath to detect process type",
                "Rootless: Disabled injection into WebContent due to ongoing issues with ElleKit",
                "Rootful: Fixed theming not working on iOS 12"
            ]]
        ],
        "description": "<p><b>**EmojiPort needs to be installed if you also want new emojis.**</b><br/>\
            This tweak allows you to theme emoji font without touching filesystem.\
            Access <b>Settings app &gt; EmojiFontManager</b> to choose your font.<br/>\
            EFM fonts must be in this format: <code>(/var/jb)/Library/Themes/EmojiFontManager/&lt;Font-Name&gt;.font/AppleColorEmoji@2x.ttc</code><br/>\
            It is highly recommended to respring after you change the font.</p>"
    },
    {
        "file": "efmfontdl",
        "title": "EFM Font Downloader",
        "changes": [
            ["1.0.4", "Fallback to cURL if downloading using wget fails"]
        ],
        "description": "<p>A simple shell script to download an emoji font for EFM from GitHub releases.</p>"
    },
    {
        "file": "emojilayout",
        "title": "EmojiLayout",
        "min_ios": "6.0",
        "max_ios": "8.2",
        "strict_range": True,
        "no_sileo": True,
        "changes": [
            ["1.2.0", "Compiled with ARC, iOS 6 minimum compatibility as of this version"],
            ["1.1.21", "Recognizes iPad emoji landscape keyboard variant"]
        ],
        "description": "<p>Layout emoji keyboard. Specifically, set number of rows and columns of emoji display.</p>"
    },
    {
        "file": "emojilibrary",
        "title": "EmojiLibrary",
        "min_ios": "5.1",
        "changes": [
            ["1.6.2", [
                "Fixed crash on iOS 6 due to using modern-only libroot",
                "Fixed incorrect glyphs for 0 - 9, * and # emojis on iOS 6"
            ]],
            ["1.6.1", "Removed misspelled and rather unused function"],
            ["1.6.0", [
                "iOS 17.4 emojis support",
                "(iOS 13.2+) Fixed silhouette hand-holding emojis not being silhouettes",
                "Refactored for better code maintainability"
            ]]
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
            ["1.0.11", "Depends on EmojiLibrary 1.6.1+"],
            ["1.0.10", "Adopted fixes related to emoji split keyboard from EmojiPort (iOS 6.0-8.2)"]
        ],
        "description": "<p>Latest emojis for iOS 5.1</p>\
            <p>This EmojiPort variant ports some of the iOS 6 variant for best compatibility on iOS 5. The manual way is recommended, as written in <a href=\"https://poomsmart.github.io/emojiport\">here</a>.</p>"
    },
    {
        "file": "emojiport_6",
        "title": "EmojiPort (iOS 6.0 - 8.2)",
        "min_ios": "6.0",
        "max_ios": "8.2",
        "strict_range": True,
        "no_sileo": True,
        "changes": [
            ["1.8.6", "Removed unused code for each architecture"],
            ["1.8.5", "Compiled with ARC"],
            ["1.8.4", "Fixed crash on iOS 6 due to using modern-only libroot"],
            ["1.8.3", "Depends on EmojiLibrary 1.6.1+"],
            ["1.8.2", [
                "Fixed emoji category images not displaying correctly",
                "Updated for new EmojiLibrary"
            ]]
        ],
        "description": "<p>Latest emojis for iOS 6.0 - 8.2</p>\
                <p><a href=\"https://poomsmart.github.io/emojiport\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojiport_8_9",
        "title": "EmojiPort (iOS 8.3 - 9.3)",
        "min_ios": "8.3",
        "max_ios": "9.3.6",
        "strict_range": True,
        "no_sileo": True,
        "changes": [
            ["1.7.1", [
                "Combined with EmojiPort (iOS 8.3 - 8.4)",
                "Updated for new EmojiLibrary"
            ]]
        ],
        "description": "<p>Latest emojis for iOS 8.3 - 9.3</p>\
            <p><a href=\"https://poomsmart.github.io/emojiport\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojiport_10",
        "title": "EmojiPort (iOS 10.0 - 11.4)",
        "min_ios": "10.0",
        "max_ios": "11.4.1",
        "strict_range": True,
        "changes": [
            ["1.4.2", "Depends on EmojiLibrary 1.6.1+"],
            ["1.4.1", [
                "Updated for new EmojiLibrary",
                "Depends on EmojiPort Resources (iOS 10+) 1.5.0+",
                "Use _NSGetExecutablePath to detect process type"
            ]]
        ],
        "description": "<p>Latest emojis for iOS 10.0 - 11.4</p>\
            <p><a href=\"https://poomsmart.github.io/emojiport\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojiport_12",
        "title": "EmojiPort (iOS 12.0 - 17.3)",
        "min_ios": "12.0",
        "max_ios": "17.3.1",
        "strict_range": True,
        "featured_as_banner": True,
        "changes": [
            ["1.5.2", [
                "(Rootless-only) Removed unnecessary hooks",
                "Use more correct type encoding for the added methods"
            ]],
            ["1.5.1", "Depends on EmojiLibrary 1.6.1+"],
            ["1.5.0~b3", [
                "Initial iOS 17.4 emojis support",
                "Updated for new EmojiLibrary"
            ]],
            ["1.4.3", [
                "Depends on EmojiPort Resources (iOS 10+) 1.5.0+",
                "Use _NSGetExecutablePath to detect process type",
                "Fixed tweak not loading on some rootful devices",
                "(Rootless-only) Disabled injection into WebContent due to ElleKit issues",
                "Allow installation on iOS 15.4 - 16.3.1",
                "Fixed app crash on rootful palera1n devices"
            ]]
        ],
        "description": "<p>Latest emojis for iOS 12.0 - 17.3</p>\
            <p><a href=\"https://poomsmart.github.io/emojiport\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojisearchforipad",
        "title": "Emoji Search for iPad",
        "min_ios": "14.0",
        "max_ios": "14.4.2",
        "strict_range": True,
        "screenshots": True,
        "description": "<p>Enable emoji search on iPadOS 14.0 - 14.4</p>"
    },
    {
        "file": "emojiskinprefs",
        "title": "EmojiSkinPrefs",
        "min_ios": "8.3",
        "screenshots": True,
        "description": "<p>Change the default skin tone of emojis.</p>"
    },
    {
        "file": "emojifontefm",
        "title": "AppleColorEmoji Unicode 15.1 (EFM)",
        "changes": [
            ["15.1.0", "Updated to Unicode 15.1"]
        ],
        "description": "<p>Unicode 15.1 (iOS 17.4) Apple's AppleColorEmoji font for EmojiFontManager.</p><br/>\
            <p>Regular version of this font has all emoji images in PNG format and better compressed than Apple's EMJC image compression.</p><br/>\
            <p>HD version of this font includes additional 160x160 PNG emoji images. They work best if you like large emojis.</p>"
    },
    {
        "file": "emojifontlqefm",
        "title": "AppleColorEmoji Low Quality (EFM)",
        "screenshots": True,
        "changes": [
            ["15.1.0", "Updated to Unicode 15.1"]
        ],
        "description": "<p>It's your usual AppleColorEmoji font but low quality. But Why? To save you some disk space? To improve your device performance? To show off your friends?</p><br/>\
            <p>All not quite. It's because sometimes you need not a high quality work to cause <a href=\"https://www.youtube.com/watch?v=7Qxa19ODUIQ\">a global impact such as this one</a>.</p><br/>\
            <p>Unicode version will be in sync with the regular Apple emoji font.</p>"
    },
    {
        "file": "emojifontflipefm",
        "title": "AppleColorEmoji HD Flip (EFM)",
        "screenshots": True,
        "description": "<p>It's your usual AppleColorEmoji font but everything is flipped horizontally.</p><br/>\
            <p>Unicode version will be in sync with the regular Apple emoji font.</p>"
    },
    {
        "file": "emojifontpxefm",
        "title": "AppleColorEmoji Pixel (EFM)",
        "screenshots": True,
        "description": "<p>It's your usual AppleColorEmoji font but everything is pixelated.</p><br/>\
            <p>Unicode version will be in sync with the regular Apple emoji font.</p>"
    },
    {
        "file": "blobmojiefm",
        "title": "Blobmoji Unicode 15.1 (EFM)",
        "screenshots": True,
        "changes": [
            ["15.1.0", "Updated to Unicode 15.1"]
        ],
        "description": "<p>Blobmoji emoji font (Blobified version of Google Noto Emoji) for EmojiFontManager (Unicode 15.1).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p><br/>\
            <p>Refer to <a href=\"https://github.com/C1710/blobmoji/blob/main/LICENSE\">here</a> for licensing.</p>"
    },
    {
        "file": "fbemojiefm",
        "title": "Facebook Emoji Unicode 15.0 (EFM)",
        "screenshots": True,
        "changes": [
            ["15.0.0", "Updated to Unicode 15.0"]
        ],
        "description": "<p>Facebook emoji font for EmojiFontManager (Unicode 15.0).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p><br/>"
    },
    {
        "file": "fluentuiefm",
        "title": "FluentUI Emoji Unicode 15.1 (EFM)",
        "screenshots": True,
        "changes": [
            ["15.1.0", "Updated to Unicode 15.1"]
        ],
        "description": "<p>Windows 11 FluentUI emoji font for EmojiFontManager (Unicode 15.1).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p>"
    },
    {
        "file": "joypixelsefm",
        "title": "JoyPixels Emoji Unicode 15.1 (EFM)",
        "screenshots": True,
        "changes": [
            ["15.1.0", "Updated to JoyPixels 9.0 (Unicode 15.1)"]
        ],
        "description": "<p>JoyPixels emoji font for EmojiFontManager (Unicode 15.1).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p><br/>\
            <p>Refer to <a href=\"https://joypixels.com/licenses/free\">here</a> for licensing.</p>"
    },
    {
        "file": "joypixelsdecalefm",
        "title": "JoyPixels Decal Emoji Unicode 15.1 (EFM)",
        "screenshots": True,
        "changes": [
            ["15.1.0", "Updated to JoyPixels 9.0 (Unicode 15.1)"]
        ],
        "description": "<p>JoyPixels emoji font (with Decal) for EmojiFontManager (Unicode 15.1).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p><br/>\
            <p>Refer to <a href=\"https://joypixels.com/licenses/free\">here</a> for licensing.</p>"
    },
    {
        "file": "notoemojiefm",
        "title": "Noto Color Emoji Unicode 15.1 (EFM)",
        "screenshots": True,
        "changes": [
            ["15.1.0", "Updated to Unicode 15.1"]
        ],
        "description": "<p>Google Noto Color emoji font for EmojiFontManager (Unicode 15.1).</p><br/>\
            <p>Refer to <a href=\"https://github.com/googlefonts/noto-emoji/blob/main/LICENSE\">here</a> for licensing.</p>"
    },
    {
        "file": "notoemojicursedefm",
        "title": "Noto Color Emoji Cursed Unicode 15.1 (EFM)",
        "changes": [
            ["15.1.0", "Updated to Unicode 15.1"]
        ],
        "description": "<p>Google Noto Color Cursed emoji font for EmojiFontManager (Unicode 15.1).</p><br/>\
            <p>Try it for yourself... it's cursed.</p>"
    },
    {
        "file": "openmojiefm",
        "title": "OpenMoji Unicode 15.0 (EFM)",
        "screenshots": True,
        "changes": [
            ["15.0.0", "Updated to Unicode 15.0"]
        ],
        "description": "<p>OpenMoji emoji font for EmojiFontManager (Unicode 15.0).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p><br/>\
            <p>Refer to <a href=\"https://github.com/hfg-gmuend/openmoji/blob/master/LICENSE.txt\">here</a> for licensing.</p>"
    },
    {
        "file": "oneuiefm",
        "title": "Samsung One UI Unicode 15.1 (EFM)",
        "screenshots": True,
        "changes": [
            ["15.1.0~beta7", "Updated to One UI 6 beta 7"]
        ],
        "description": "<p>Samsung One UI (6 beta) emoji font for EmojiFontManager (Unicode 15.1).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p>"
    },
    {
        "file": "tossfaceefm",
        "title": "Toss Face Unicode 15.0 (EFM)",
        "screenshots": True,
        "changes": [
            ["15.0.0", "Updated to Unicode 15.0"]
        ],
        "description": "<p>Toss Face (토스페이스) emoji font for EmojiFontManager (Unicode 15.0).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p><br/>\
            <p>Refer to <a href=\"https://toss.im/tossface\">here</a> for licensing.</p>"
    },
    {
        "file": "twemojiefm",
        "title": "Twemoji Unicode 15.1 (EFM)",
        "screenshots": True,
        "changes": [
            ["15.1.0", "Updated to Unicode 15.1"]
        ],
        "description": "<p>Twitter Twemoji emoji font for EmojiFontManager (Unicode 15.1).</p>"
    },
    {
        "file": "whatsappefm",
        "title": "WhatsApp Emoji Unicode 15.1 (EFM)",
        "screenshots": True,
        "changes": [
            ["15.1.0", "Updated to Unicode 15.1"]
        ],
        "description": "<p>WhatsApp emoji font for EmojiFontManager (Unicode 15.1).</p><br/>\
            <p>Refer to <a href=\"https://github.com/PoomSmart/EmojiFonts/blob/main/CAVEATS.md\">here</a> for known issues and limitations.</p>"
    },
]
