# pip3 install jinja2 minify-html --user
from jinja2 import Environment, FileSystemLoader
import os, re, json, html, minify_html

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
screenshots_dir = os.path.join(root, 'screenshots')
env = Environment(loader=FileSystemLoader(templates_dir), trim_blocks=True, lstrip_blocks=True)
html_template = env.get_template('index.html')

def tweak_url(name):
    return f"https://poomsmart.github.io/repo/depictions/{name}"

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
        "file": "emojiattributes",
        "title": "EmojiAttributes",
        "min_ios": "5.1",
        "changes": [
            [ "1.4.5", "Stripped unneeded hacks" ]
        ],
        "description": "<p>Various under-the-hood fixes for emoji display. See <a href=\"https://github.com/PoomSmart/EmojiAttributes/blob/master/README.md\">here</a> for more information.</p>"
    },
    {
        "file": "emojiport10resources",
        "title": "emojiport10resources",
        "min_ios": "10.0",
        "changes": [
            [ "1.2.6", "Updated to iOS 15.0 assets" ]
        ],
        "description": "<p>Up-to-date emoji assets (bitmap, localization, metadata, translation) for iOS 10 and above.</p>"
    },
    {
        "file": "emojifontmanager",
        "title": "EmojiFontManager",
        "min_ios": "6.0",
        "changes": [
            [ "1.1.2", "Fixed buttons not working" ],
            [ "1.1.1", "Compiled with ARC" ],
            [ "1.0.0", "Reworked Settings page for better visual in recent iOS versions" ]
        ],
        "description": "<p><b>**EmojiPort needs to be installed if you also want new emojis.**</b><br/>\
            This tweak allows you to theme emoji font wihout touching filesystem.\
            Access <b>Settings app &gt; EmojFontManager</b> to choose your font.<br/>\
            EFM fonts must be in this format: <code>/Library/Themes/EmojiFontManager/&lt;Font-Name&gt;.font/AppleColorEmoji@2x.{ttf,ttc}</code><br/>\
            It is highly recommended to respring after you change the font.</p>"
    },
    {
        "file": "emojilayout",
        "title": "EmojiLayout",
        "min_ios": "5.1",
        "max_ios": "8.2",
        "strict_range": True,
        "no_sileo": True,
        "changes": [
            [ "1.1.21", "Recognizes iPad emoji landscape keyboard variant" ]
        ],
        "description": "<p>Layout emoji keyboard. Specifically, set number of rows and columns of emoji display.</p>"
    },
    {
        "file": "emojilibrary",
        "title": "EmojiLibrary",
        "min_ios": "5.1",
        "changes": [
            [ "1.3.0", "Compiled with ARC" ]
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
            [ "1.7.5", "Fixed crashing when selecting skinned emojis" ]
        ],
        "description": "<p>Latest emojis for iOS 6.0 - 8.2</p>\
                <p><a href=\"https://poomsmart.github.io/emojiport\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
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
                <p><a href=\"https://poomsmart.github.io/emojiport\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
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
            <p><a href=\"https://poomsmart.github.io/emojiport\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
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
            <p><a href=\"https://poomsmart.github.io/emojiport\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "emojiport_12",
        "title": "EmojiPort (iOS 12.0 - 14.4)",
        "min_ios": "12.0",
        "max_ios": "14.4.2",
        "strict_range": True,
        "featured_as_banner": True,
        "changes": [
            [ "1.1.2", "Improved hooks" ],
            [ "1.1.1", "Release version" ]
        ],
        "description": "<p>Latest emojis for iOS 12.0 - 14.4</p>\
            <p><a href=\"https://poomsmart.github.io/emojiport\">** Follow instructions on installing emoji font here, otherwise emojis will render incorrectly**</a></p>"
    },
    {
        "file": "letmeblock",
        "title": "LetMeBlock",
        "min_ios": "9.0",
        "changes": [
            [ "1.0.0", "Increased Jetsam memory limit to 512 MB" ],
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
        "featured_as_banner": True,
        "changes": [
            [ "1.0.2", "Fixed crashing on iOS 12 when opening flashlight CC module" ],
            [ "1.0.1", "Compiled Amber CC Module with ARC" ],
            [ "1.0.0", "Amber Flipswitch now includes arm64e slice" ]
        ],
        "description": "<p>A CC module/Flipswitch tweak to allow setting of Amber LED, or both White and Amber LEDs.</p>"
    },
    {
        "file": "quadhighcurrent",
        "title": "QuadHighCurrent",
        "min_ios": "10.0",
        "changes": [
            [ "1.0.0",
                [
                    "Fixed blackout settings icon when dark mode is active",
                    "Added arm64e slice to the Flipswitch module"
                ]
            ]
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
        "file": "padgrid",
        "title": "PadGrid",
        "min_ios": "7.0",
        "description": "<p>Increase home screen icon grid size for iPad.</p>",
        "changes": [
            [ "1.0.3", "Added Custom rows and columns option" ],
            [ "1.0.2", "Added 9x6, 10x7 and 10x8 layouts" ],
            [ "1.0.1", "Added IconAnus and Icon Layout Manager as alternative dependencies to IconState" ]
        ]
    },
    {
        "file": "splitit",
        "title": "SplitIt",
        "min_ios": "10.0",
        "max_ios": "13.7",
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
            [ "1.0.0", "Fixed issues with GoodNotes 5 app" ]
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
        "has_source_code": True,
        "description": "<p>Default size of Animoji/Memoji stickers is no more than 500px * 500px and the stickers look too pixellated. This tweak will simply double the size.</p>",
        "changes": [
            [ "1.0.0", "Supports WWDC 2021 Developer Stickers" ]
        ]
    },
    {
        "file": "ytuhd",
        "title": "YTUHD",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Unlock 1440p and 2160p resolutions (VP9-compatible) in iOS YouTube app.</p>",
        "changes": [
            [ "1.2.5", "Fixed crashing on some older YouTube versions" ],
            [ "1.2.4", "Forces enabling Video quality settings on older YouTube to have YTUHD setting there" ],
            [ "1.2.3", "Added back support for iOS 11 and 12" ],
            [ "1.2.2",
                [
                    "Forces using local ABR rather than server to allow for UHD resolutions",
                    "Fixed YTUHD setting doesn't display on YouTube 15.33.4 or lower"
                ]
            ],
            [ "1.2.0", "Make A10/A10X and lower devices use hardware acceleration for VP9" ],
            [ "1.1.2", "Simplified logic in settings creation" ],
            [ "1.1.1",
                [
                    "Added in-app settings for using VP9 codec (Settings > Video quality preferences)",
                    "Deprecated support for iOS 11 - 12",
                    "Spoof OS version to 14.7 for iOS/iPadOS 13"
                ]
            ],
            [ "1.0.2",
                [
                    "Spoof iOS version to 14.6 for those on iOS 11 - 13",
                    "Compiled with ARC"
                ]
            ],
            [ "1.0.1", "Removed render view type override" ]
        ]
    },
    {
        "file": "youpip",
        "title": "YouPiP",
        "min_ios": "11.0",
        "tintColor": "red",
        "featured_as_banner": True,
        "description": "<p>Enable native PiP in YouTube app.</p>\
            <p>If you encounter playback speedup issue for your PiP, try to upgrade to YouPiP 1.4.3+ (and enable Sample Buffer Hack in YouPiP settings) or use iOS 15.0b2+.</p>\
            <p>If you encounter \"No stream Tap to Retry\" error for your video, you are recommended to upgrade YouTube to the latest version.</p>",
        "changes": [
            [ "1.5.15", "Fixed support for iOS 12 (and probably iOS 11)" ],
            [ "1.5.14", "Make Legacy PiP enabled by default for iOS 11/12 (regression fix for 1.5.13)" ],
            [ "1.5.12", "Make PiP toggle displays for non-premium users on YouTube 16.40.3" ],
            [ "1.5.11",
                [
                    "Known issue: PiP may not work on iOS 12",
                    "Fixed crashing on some older YouTube versions",
                    "Enforces legacy video decoder when legacy PiP is enabled"
                ]
            ],
            [ "1.5.10",
                [
                    "Compiled with iOS 15.0 SDK",
                    "Inject PiP controller into YTAutonavEndscreenController for better iOS 13- compatibility"
                ]
            ],
            [ "1.5.9", "Fixed PiP controller not working on iOS 13- in recent YouTube versions" ],
            [ "1.5.8", "Minor code optimizations" ],
            [ "1.5.7", "Fixed YouPiP settings not showing on older versions of YouTube" ],
            [ "1.5.6 (15.10.4+)", "Fixed crashing on YouTube version 16.29.4" ],
            [ "1.5.5", "Fixed YouPiP settings being unsynchronized when other native settings are toggled" ],
            [ "1.5.4 (15.10.4 - 16.28.2)",
                [
                    "Fixed PiP still being activated when \"Use PiP Button\" is on, on app dismiss",
                    "\"Non-backgroundable PiP\" option will only be displayed on YouTube versions that support it",
                    "PiP button now shows or hides according to the setting"
                ]
            ],
            [ "1.5.2",
                [
                    "Migrated YouPiP settings into YouTube's native settings (Settings > General)",
                    "Added \"Non-backgroundable PiP\" option in settings"
                ]
            ],
            [ "1.4.11 (15.10.4+)", 
                [
                    "Added backward compatibility with YouTube 15.10.4",
                    "Removed potentially unneeded hooks"
                ]
            ],
            [ "1.4.10", "Fixed PiP activating on app dismiss even when the mode is \"On PiP button tap\" issue introduced in 1.4.9" ],
            [ "1.4.9",
                [
                    "Refactored logic around PiP activation via button tap",
                    "Reworked settings page"
                ]
            ],
            [ "1.4.8", "YouPiP no longer dismisses the app automatically when PiP is activated from the button because the legacy app assertion leads to PiP closing itself" ],
            [ "1.4.7",
                [
                    "Fixed crashing on YouTube version 15.49.6 (and maybe lower)",
                    "Fixed crashing on iOS/iPadOS 14.0-14.1 for YouTube version 16.25.2"
                ]
            ],
            [ "1.4.5", "Force-enabled YouTube's enablePipForNonBackgroundableContent flag that may fix PiP crashing issue for some people" ],
            [ "1.4.4", "Added Sample Buffer Hack in settings (iOS/iPadOS 14)" ],
            [ "1.4.3",
                [
                    "Fixed app crashing on some versions of iOS/iPadOS 14",
                    "Added a warning alert if YouTube version is lower than the lowest supported"
                ]
            ],
            [ "1.4.2", "Fixed PiP not working on iOS/iPadOS 14.0 - 14.4 for YouTube 16.25.2" ],
            [ "1.4.1", "Added few more missing logic from iOS 15.0b2 approach" ],
            [ "1.4.0", "Attempted to fix PiP playback speedup bug using iOS 15.0b2 approach" ],
            [ "1.3.4", "Enable native PiP toggle inside YouTube settings" ],
            [ "1.3.3", "Refactored logic related to bootstraping PiP functionality" ],
            [ "1.3.2", "Fixed crashing due to adding PiP button to the overlay for some users" ],
            [ "1.3.1",
                [
                    "Fixed crash on YouTube version 15.49.6",
                    "Added legacy PiP implementation in settings"
                ]
            ],
            [ "1.2.3", "Removed armv7 slice as YouTube targets iOS 11 and above" ],
            [ "1.2.2 (15.19.4+)", "Added backward compatibility with YouTube 15.22.4" ],
            [ "1.2.1", "\"On PiP button tap\" should no longer make PiP activated on app dismiss (iOS/iPadOS 14+)" ],
            [ "1.2.0 (16.17.4)", "Added settings page to choose how to activate PiP" ]
        ]
    },
    {
        "file": "youmusicpip",
        "title": "YouMusicPiP",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Enable native PiP in YouTube Music app. This works for videos present in the app.</p>"
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
            [ "1.4.0", "Removed icon grid size overrides, please use PadGrid to adjust this instead" ]
        ]
    },
    {
        "file": "apppad",
        "title": "AppPad",
        "min_ios": "9.0",
        "description": "<p>Full screen, Split and Slideover for every app on iPad.</p>",
        "changes": [
            [ "1.1.0", "Use AltList classless approach" ],
            [ "1.0.0", "Use AltList for listing applications" ],
            [ "0.0.2", "You can now configure blacklisted applications from Settings" ],
            [ "0.0.1", "Initial release" ]
        ]
    },
    {
        "file": "ytclassicvideoquality",
        "title": "YTClassicVideoQuality",
        "min_ios": "11.0",
        "tintColor": "red",
        "has_source_code": True,
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
        "tintColor": "orange",
        "has_source_code": True,
        "description": "<p>Restore the original buttons layout in Instagram; Home-Search-Compose-Likes-Profile at bottom and Messages at top.</p>",
        "changes": [
            [ "1.0.1", "Remove top Reels section in Search page" ]
        ]
    },
    {
        "file": "nottodayhomescreensidebar",
        "title": "NotTodayHomeScreenSideBar",
        "min_ios": "14.0",
        "max_ios": "14.8.1",
        "strict_range": True,
        "screenshots": True,
        "featured_as_banner": True,
        "has_source_code": True,
        "description": "<p>Prevent Today View sidebar from being pinned on iPad homescreen. Widgets in Today View will still be accessible by swiping to the leftmost of the homescreen, just like how it is on iPad portrait or iPhone.</p>"
    },
    {
        "file": "expandedclassicscreen",
        "title": "expandedclassicscreen",
        "min_ios": "14.0",
        "screenshots": True,
        "has_source_code": True,
        "description": "<p>Use a larger 414x736 (iPhone 6s+) resolution for classic apps on iPad.</p>"
    },
    {
        "file": "lpmenabler",
        "title": "LPM Enabler",
        "min_ios": "11.0",
        "max_ios": "14.8.1",
        "tintColor": "yellow",
        "strict_range": True,
        "has_source_code": True,
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
        "has_source_code": True,
        "description": "<p>Toggle Wi-Fi and Bluetooth On/Off explicitly from Control Center on iOS 11+.</p>",
        "changes": [
            [ "1.0.0", "Compiled with ARC" ],
            [ "0.0.1.1", "Initial release" ]
        ]
    },
    {
        "file": "ytsystemappearance",
        "title": "YTSystemAppearance",
        "min_ios": "13.0",
        "tintColor": "red",
        "has_source_code": True,
        "description": "<p>Enable setting appearance (Light/Dark) based on system in YouTube app. Because this feature is based on iOS dark mode, the tweak only supports iOS/iPadOS 13 and above. YouTube version 15.10.4 and higher are officially supported. Older (but not too old) versions may.</p>"
    },
    {
        "file": "ytreexplore",
        "title": "YTReExplore",
        "min_ios": "11.0",
        "tintColor": "red",
        "screenshots": True,
        "description": "<p>Remove Shorts tab and replace with Explore tab in YouTube app.</p>\
            <p>This tweak is mostly for iPhones and iPods where Explore is replaced with Shorts.</p>\
            <p>Limitation: The text \"Explore\" is hardcoded in English because its localization is entirely from server-side.</p>",
        "changes": [
            [ "1.0.2", "Supports YouTube 16.45.4" ],
            [ "1.0.1", "Minor optimization" ]
        ]
    },
    {
        "file": "youarethere",
        "title": "YouAreThere",
        "min_ios": "11.0",
        "tintColor": "red",
        "has_source_code": True,
        "description": "<p>Disable \"Video paused. Continue watching?\" popup in YouTube app when you play a long video.</p>"
    },
    {
        "file": "noytpremium",
        "title": "noytpremium",
        "min_ios": "11.0",
        "tintColor": "red",
        "has_source_code": True,
        "description": "<p>Remove YouTube Premium upsells.</p>",
        "changes": [
            [ "1.0.3", "Removed \"Try new features\" from YouTube settings" ],
            [ "1.0.2", "Hook more methods" ]
        ]
    },
    {
        "file": "noytmpremium",
        "title": "noytmpremium",
        "min_ios": "11.0",
        "tintColor": "red",
        "has_source_code": True,
        "description": "<p>Remove YouTube Music Premium upsell elements (banner, alerts, tab item).</p>"
    },
    {
        "file": "youremembercaption",
        "title": "youremembercaption",
        "min_ios": "11.0",
        "tintColor": "red",
        "has_source_code": True,
        "description": "<p>Make YouTube remember your video caption setting, if not already.</p>"
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
        "file": "expandlesscamcontrols",
        "title": "expandlesscamcontrols",
        "min_ios": "9.0",
        "has_source_code": True,
        "description": "<p>Adjust Flash/HDR/Timer in Camera (with old UI) with less finger travel. <a href=\"https://twitter.com/PoomSmart/status/1429331330903408645\">Demo video</a>.</p>"
    },
    {
        "file": "ytnochecklocalnetwork",
        "title": "YTNoCheckLocalNetwork",
        "min_ios": "11.0",
        "tintColor": "red",
        "has_source_code": True,
        "screenshots": True,
        "description": "<p>Remove Local Network permission check in YouTube app.</p>"
    },
    {
        "file": "ytabgoodies",
        "title": "YTABGoodies",
        "min_ios": "11.0",
        "tintColor": "red",
        "has_source_code": True,
        "description": "<p>YouTube usually implements a feature as an experiment. You may get to see it while others don't, and vice-versa.\
            This tweak will enable or disable those features in a way useful to you.\
            This replaces the following tweaks:</p>",
        "extra_content": "<ul>\
                <li><a href=\"{}\">YouAreThere</a></li>\
                <li><a href=\"{}\">YouRememberCaption</a></li>\
                <li><a href=\"{}\">YTNoCheckLocalNetwork</a></li>\
                <li><a href=\"{}\">YTSystemAppearance</a></li>\
            </ul>".format(
                tweak_url("youarethere"),
                tweak_url("youremembercaption"),
                tweak_url("ytnochecklocalnetwork"),
                tweak_url("ytsystemappearance")
            )
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
            [ "1.1.0", "Added support for an array of Metal-based apps" ],
            [ "1.0.3",
                [
                    "Added arm64e slice",
                    "Separate system and user apps in sections"
                ]
            ],
            [ "1.0.1", "Enforces the value of preferredFramesPerSecond to zero (highest)" ]
        ]
    },
    {
        "file": "injectionfoundation",
        "title": "Injection Foundation",
        "min_ios": "7.0",
        "description": "<p>Inject UIKit tweaks into Foundation apps. Check out the source code for how it works and the motivation behinds on <a href=\"https://github.com/PoomSmart/Injection-Foundation\">GitHub</a>.</p>",
    }
]

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
    has_source_code = entry.get("has_source_code")
    debug = entry.get("debug")
    description = re.sub(r'\s+', ' ', entry.get("description"))
    extra_content = entry.get("extra_content")
    if extra_content:
        extra_content = re.sub(r'\s+', ' ', extra_content)
    output_path = os.path.join(root, "depictions", "%s.html" % file)

    source_code = None
    screenshot_objects = list(map(
        lambda e: {
            "url": "https://poomsmart.github.io/repo/screenshots/%s/%s" % (file, e.name),
            "accessibilityText": e.name
        },
        os.scandir(os.path.join(screenshots_dir, file))
    )) if screenshots else None

    if has_source_code:
        try:
            with open("../../%s/Tweak.x" % file, 'r') as source_code_content:
                source_code = source_code_content.read()
        except IOError:
            print("Could not read source code of %s" % title)

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
            source_code=html.escape(source_code) if source_code is not None else None,
            debug=debug
        ), minify_js=False, minify_css=False))
    print("Generated %s" % output_path)

    no_sileo = entry.get("no_sileo")
    if no_sileo:
        continue
    sileo_output_path = os.path.join(root, "sileodepictions", "%s.json" % file)
   
    with open(os.path.join(templates_dir, "index.json")) as json_file:  
        data = json.load(json_file)
        for key in sileo_keys:
            val = entry.get(key)
            if val:
                data[key] = val
        if featured_as_banner and 'headerImage' not in entry:
            data['headerImage'] = "https://poomsmart.github.io/repo/features/%s.png" % file
        tabs = data["tabs"]
        for json_entry in tabs:
            tabname = json_entry["tabname"]
            if tabname == "Details":
                views = json_entry["views"]
                views[0]["markdown"] = description
                if screenshot_objects is not None and screenshot_objects.count:
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
        if min_ios:
            support_versions = {
                "class": "DepictionSubheaderView",
                "useMargins": True,
                "title": "Compatible with iOS %s to %s" % (min_ios, max_ios) if min_ios and max_ios else "Compatible with iOS %s +" % min_ios
            }
            views.insert(0, support_versions)
        if source_code:
            source_code_tab = {
                "class": "DepictionStackView",
                "tabname": "Source Code",
                "views": [
                    {
                        "class": "DepictionMarkdownView",
                        "markdown": "```\n%s\n```" % source_code
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
