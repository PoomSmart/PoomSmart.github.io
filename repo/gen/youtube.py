from helper import *

youtube = [
    {
        "file": "ytuhd",
        "title": "YTUHD",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Unlock 1440p and 2160p resolutions (VP9-compatible) in iOS YouTube app.</p>",
        "changes": [
            ["1.4.3", [
                "Updated spoof version to 15.8.1 (for iOS 14-)",
                "Updated zh_cn localization"
            ]],
            ["1.4.2", "Fixed crash on YouTube 19.03.2 and higher"],
            ["1.4.1", [
                "Updated spoof version to 15.8 (for iOS 14-)",
                "Added note about YouPiP tweak when used in conjunction with YTUHD",
                "Added th localization"
            ]],
            ["1.4.0-1", [
                "Force VP9 formats only for 1440p and higher",
                "Updated spoof version to 15.7.6 (for iOS 14-)",
                "Updated ja localization"
            ]],
            ["1.3.5", [
                "Updated spoof version to 15.7.2 (for iOS 14-)",
                "Updated tr, zh_cn localization"
            ]],
            ["1.3.4-2", "Added ar, de, fr, hu, it, ja, ko, nl, pt, ro, ru, tr, vi, zh_cn, zh_tw localization"],
            ["1.2.10", "Prevent the app from choosing AVC1 over VP9 codec"],
            ["1.2.9", [
                "Hooks MLABRPolicyNew and MLABRPolicyOld classes (introduced in YouTube 17.30.3)",
                "Updated spoofed version to iOS 15.6 (for iOS 13-)"
            ]],
            ["1.2.8", "Reverted non-HDR 720p+ workaround because YouTube has fixed the issue"],
            ["1.2.7", [
                "Allows non-HDR 720p+ formats of UHD HDR videos to display as options (for iOS 14/sideloaded?)",
                "Updated spoofed version to iOS 15.4.1 (for iOS 13-)"
            ]],
            ["1.2.6", "Updated spoofed version to iOS 14.8.1 (for iOS 13-)"],
            ["1.2.5", "Fixed crashing on some older YouTube versions"],
            ["1.2.4", "Forces enabling Video quality settings on older YouTube to have YTUHD setting there"]
        ]
    },
    {
        "file": "youpip",
        "title": "YouPiP",
        "min_ios": "11.0",
        "tintColor": "red",
        "featured_as_banner": True,
        "description": "<p>Enable native PiP in iOS YouTube app.</p>\
            <p>YouPiP best supports the latest version of YouTube. You may downgrade to as far as version 15.10.4 but full compatibility for older versions is low-priority.</p>",
        "changes": [
            ["1.8.4", "Improved compatibility with iOS 14 and lower"],
            ["1.8.3", "Improved the logic to add PiP button to the video tab bar (contributed by NguyenASang)"],
            ["1.8.2", "Fixed crash on YouTube 19.03.2 and higher"],
            ["1.8.1", "Fixed PiP button in video tab bar not colored correctly for new YouTube versions"],
            ["1.8.0", "Added PiP button to video tab bar for new YouTube versions (contributed by NguyenASang)"],
            ["1.7.22", [
                "Fixed Legacy PiP compatibility on YouTube 18.41.2 and higher",
                "Known issue: Non-Legacy PiP may not work on iOS 14 and lower on recent YouTube versions"
            ]],
            ["1.7.21", "Corrected type encoding for the added methods"],
            ["1.7.19-2", [
                "You may now enable or disable YouPiP from its settings",
                "Updated ar localization"
            ]],
            ["1.7.18", "Fixed PiP not activating for some people"],
            ["1.7.17", "Fixed \"Fake YouTube version\" not restoring the old video bar for some people"],
            ["1.7.16 (15.10.4+)", "Fixed crashing when activating PiP with \"Legacy PiP\" enabled on recent YouTube versions"]
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
        "file": "ytclassicvideoquality",
        "title": "YTClassicVideoQuality",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Revert to the original video quality selector in YouTube app.</p>",
        "changes": [
            ["1.2.0", "Added Premium formats to the classic video quality selector, if the video supports it"],
            ["1.1.0", "Use an alternative method to restore the video quality selector"],
            ["1.0.1", "Fixed crashing in YouTube 16.20.5"]
        ]
    },
    {
        "file": "ytsystemappearance",
        "title": "YTSystemAppearance",
        "min_ios": "13.0",
        "tintColor": "red",
        "inline_source_code": True,
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
            ["1.0.2", "Supports YouTube 16.45.4"]
        ]
    },
    {
        "file": "ytshortsprogress",
        "title": "YTShortsProgress",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Always enable progress bar and scrubbing in YouTube Shorts.</p>",
        "changes": [
            ["1.0.3", "Added more hooks (contributed by @dayanch96)"],
            ["1.0.2", "Fixed a bug where swiping on a full-screen video always triggers progress bar change"]
        ]
    },
    {
        "file": "youarethere",
        "title": "YouAreThere",
        "min_ios": "11.0",
        "tintColor": "red",
        "inline_source_code": True,
        "description": "<p>Disable \"Video paused. Continue watching?\" popup in YouTube app when you play a long video.</p>"
    },
    {
        "file": "noytpremium",
        "title": "noytpremium",
        "min_ios": "11.0",
        "tintColor": "red",
        "inline_source_code": True,
        "description": "<p>Remove YouTube Premium upsells.</p>"
    },
    {
        "file": "noytmpremium",
        "title": "noytmpremium",
        "min_ios": "11.0",
        "tintColor": "red",
        "inline_source_code": True,
        "description": "<p>Remove YouTube Music Premium upsell elements (banner, alerts, tab item).</p>"
    },
    {
        "file": "youremembercaption",
        "title": "youremembercaption",
        "min_ios": "11.0",
        "tintColor": "red",
        "inline_source_code": True,
        "description": "<p>Make YouTube remember your video caption setting, if not already.</p>"
    },
    {
        "file": "ytnochecklocalnetwork",
        "title": "YTNoCheckLocalNetwork",
        "min_ios": "11.0",
        "tintColor": "red",
        "inline_source_code": True,
        "screenshots": True,
        "description": "<p>Remove Local Network permission check in YouTube app.</p>"
    },
    {
        "file": "ytnopaidpromo",
        "title": "YTNoPaidPromo",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Remove \"Include paid promotion\" banner from videos on YouTube app.\
            <a href=\"https://www.youtube.com/watch?v=FxyW7Gp9Jd4\">What is paid promotion?</a></p>"
    },
    {
        "file": "ytabconfig",
        "title": "YTABConfig",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>YouTube usually implements a feature as an experiment. You may get to see it while others don't, and vice-versa.\
            This tweak adds a new section named \"A/B\" in the app settings where all features can be toggled freely by you.\
            There are thousands of features available. Some of them are already overridden by tweaks like YTABGoodies and its predecessors.</p>",
        "changes": [
            ["1.7.1", [
                "Fixed killswitch and grouped settings toggles not respecting the user's cancel action",
                "Refactored the code",
                "Updated es, ro and vi localization"
            ]],
            ["1.7.0", [
                "Changed the format of exported current settings to be prefixed with YT(Cold|Hot|Global)Config.",
                "The imported settings that have the same value as the current one will not be imported"
            ]],
            ["1.6.0", "You can now import the YTABConfig settings from the clipboard"],
            ["1.5.1", "Fixed crash on YouTube 19.03.2 and higher"],
            ["1.5.0-3", [
                "Added ro localization",
                "Updated de, tr localization"
            ]],
            ["1.5.0", [
                "Tap on each A/B setting to reveal its class, copy it to clipboard or delete itself from the modified list",
                "Fixed \"View modified settings\" showing outdated settings"
            ]],
            ["1.4.7", [
                "Minor optimizations",
                "Updated ja, pt, zh_cn localization"
            ]],
            ["1.4.6", [
                "Modified settings are now suffixed with \"*\"",
                "Search feature is now available only if grouped settings is disabled"
            ]],
            ["1.4.5-4", [
                "Confirmation alert will now show if you perform an action that requires quitting app",
                "Added hu, ru, zh_cn localization, Updated ar, tr, zh_tw localization"
            ]],
            ["1.4.4", [
                "Added support for YouTube 16.42.3 and lower",
                "Added search functionality (contributed by @level3tjg)",
                "Added \"Group settings by prefixes\" option",
                "Optimized the existence check of modified settings",
                "Display \"Copied to clipboard\" alert also when modified settings are copied",
                "For long-named settings on iPhone, the non-truncated version will display",
                "Added ar, ja, ko, pt, vi, zh_tw localization"
            ]],
            ["1.3.0", [
                "Categorize feature flags into short prefixes for easier navigation",
                "Supports localization"
            ]],
            ["1.2.2", "Filtered out irrelevant features starting with amsterdam and unplugged"],
            ["1.2.1", "Added settings from YTGlobalConfig class"],
            ["1.2.0", [
                "Breaking: Changed setting key format to \"YTABC.[Class].[Method]\" for future expansion but this also means you have to re-set your changes again",
                "Reduced memory footprint"
            ]],
            ["1.1.0", "Added \"View modified settings\" and \"Copy current settings\" options"]
        ]
    },
    {
        "file": "ytabgoodies",
        "title": "YTABGoodies",
        "min_ios": "11.0",
        "tintColor": "red",
        "inline_source_code": True,
        "description": "<p>YouTube usually implements a feature as an experiment. You may get to see it while others don't, and vice-versa.\
            This tweak enables or disables those features in a way useful to you.\
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
        ),
        "changes": [
            ["1.0.4", "Enabled video zoom in/out feature"]
        ]
    },
    {
        "file": "ytautofullscreen",
        "title": "YTAutoFullScreen",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Make your video full-screen on playing.</p>",
        "changes": [
            ["1.0.3", "Fixed possible crash in some cases (contributed by @bakedpotato191)"]
        ]
    },
    {
        "file": "ytsilentvote",
        "title": "YTSilentVote",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Remove popup when you like/dislike videos; those saying you liked the video and feedback shared with the creator.</p>"
    },
    {
        "file": "ytvideooverlay",
        "title": "YTVideoOverlay",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>A helper tweak to add buttons on YouTube's video overlay. Used by YouMute and YouQuality.</p>",
        "changes": [
            ["1.1.6", "Fixed the bottom buttons not showing on YouTube 16.45.4 and lower"],
            ["1.1.5", "Fixed the bottom buttons not showing for some users"],
            ["1.1.4", "Fixed crash on YouTube 19.03.2 and higher"],
            ["1.1.3", [
                "Increased the spacing between bottom buttons for better accessibility",
                "Fixed bottom buttons not positioned correctly on small iPhone devices",
            ]],
            ["1.1.2", "Fixed overlay buttons not appearing on YouTube 19.02.1 and higher"],
            ["1.1.1-2", [
                "Added de localization",
                "Updated ja localization"
            ]],
            ["1.1.1", "Fixed incorrect button positioning in some scenarios"]
        ]
    },
    {
        "file": "youmute",
        "title": "YouMute",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Add a mute button to the video overlay where you can directly mute or unmute the video.</p>",
        "changes": [
            ["1.2.1-3", "Added de, tr localization"],
            ["1.2.1", "Depends on YTVideoOverlay helper tweak"],
            ["1.1.1", "Corrected mute button position when placed at the bottom and the audio track button is visible"],
            ["1.1.0", "Added setting page, allowing you to toggle tweak and change mute button position"]
        ]
    },
    {
        "file": "youquality",
        "title": "YouQuality",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Add a video quality to the video overlay where you can easily change the video quality.</p>\
            <p>Install YTClassicVideoQuality alongside this tweak to make video quality list appear right away.</p>",
        "changes": [
            ["1.1.4-2", [
                "Added de localization",
                "Updated es localization"
            ]],
            ["1.1.4", "Make label displays for non 60 FPS 720p, 1080p, 2K and 4K"],
            ["1.1.2-1", "Added ja and tr localization"],
            ["1.1.2", "Use YouTube-styled font for the quality label (contributed by @dayanch96)"],
            ["1.1.1", "Depends on YTVideoOverlay helper tweak"],
            ["1.0.0-1", "Added ru and zh_cn localization"]
        ]
    },
    {
        "file": "ytx",
        "title": "YouTube X",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>No ads and background playback for iOS YouTube app.</p>",
        "changes": [
            ["1.5.0", "Block ads by truly setting their size to zero"],
            ["1.4.3", "Block YouTube upgrade dialog"],
            ["1.4.2", "Switched to collection view hook, Block more kinds of ads"],
            ["1.3.0", "Improved hooks"],
            ["1.2.5", "Hide statement_banner.eml ads"]
        ]
    },
    {
        "file": "yougroupsettings",
        "title": "YouGroupSettings",
        "min_ios": "14.0",
        "tintColor": "red",
        "description": "<p>Allow tweak-made settings to be grouped and displayed in iOS YouTube app. <a href=\"https://github.com/PoomSmart/YouGroupSettings\">README</a></p>"
    }
]
