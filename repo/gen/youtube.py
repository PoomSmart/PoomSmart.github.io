from helper import *

youtube = [
    {
        "file": "ytuhd",
        "title": "YTUHD",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Unlock 1440p and 2160p resolutions (VP9-compatible) in iOS YouTube app.</p>",
        "changes": [
            ["1.5.9", [
                "Made \"Use VP9\" option enabled by default",
                "Removed message about UHD resolutions not working with YouPiP from settings (v1.5.8 made it work)"
            ]],
            ["1.5.8", "Added 2K/4K formats to AVPlayer video playback (YouPiP with Legacy PiP option enabled)"],
            ["1.5.7", [
                "Translated the remaining languages using AI",
                "Removed redundant hook"
            ]],
            ["1.5.6", "Maybe Fixed an issue where a video may start with a random non-preferred caption track"],
            ["1.5.5-2", "Added id, pl localization"],
            ["1.5.5", [
                "Added a future-proof hook for when iosPlayerClientSharedConfigPostponeCabrPreferredFormatFiltering will be removed",
                "Updated spoof version to 15.8.3 (for iOS 14-)",
                "Updated ru, tr localization"
            ]],
            ["1.5.3", "Fixed 1440p+ formats not showing on YouTube version 19.24.2 and higher"],
            ["1.5.2", "Fixed crash on YouTube version 19.22.3 and higher"],
            ["1.5.1", [
                "Fixed 1440p+ formats not showing on recent YouTube versions",
                "Force enabled AV1 codec alongside VP9",
                "Updated ja localization"
            ]],
            ["1.5.0-1", [
                "Added \"VP9 for all\" option where you can enable VP9 for all resolutions",
                "Updated es and zh_cn localization"
            ]],
            ["1.4.3", [
                "Updated spoof version to 15.8.1 (for iOS 14-)",
                "Updated zh_cn localization"
            ]],
            ["1.4.2", "Fixed crash on YouTube version 19.03.2 and higher"],
            ["1.4.1", [
                "Updated spoof version to 15.8 (for iOS 14-)",
                "Added note about YouPiP tweak when used in conjunction with YTUHD",
                "Added th localization"
            ]],
            ["1.4.0-1", [
                "Force VP9 formats only for 1440p and higher",
                "Updated spoof version to 15.7.6 (for iOS 14-)",
                "Hooks MLABRPolicyNew and MLABRPolicyOld classes (introduced in YouTube version 17.30.3)",
                "Fixed crashing on some older YouTube versions",
                "Forces enabling Video quality settings on older YouTube to have YTUHD setting there"
            ]]
        ]
    },
    {
        "file": "youpip",
        "title": "YouPiP",
        "min_ios": "11.0",
        "tintColor": "red",
        "featured_as_banner": True,
        "description": "<p>Enable native PiP in iOS YouTube app.</p>\
            <p>YouPiP best supports the latest version of YouTube. You may downgrade to as far as version 16.29.4, older versions will not be (fully) supported.</p>",
        "changes": [
            ["1.12.3", "Background playback is no longer forcibly enabled for YouPiP, you should ensure it is enabled in the original YouTube app settings"],
            ["1.12.2", "Fixed Video Tab Bar PiP button being black in dark mode on YouTube version 20.02.3"],
            ["1.12.1", "Fixed the tweak setting icon being black in dark mode on YouTube version 20.02.3"],
            ["1.12.0", [
                "Simplified PiP enabling logic",
                "Fixed setting icon not appearing when the tweak is disabled and grouped settings experiment is on",
                "When iOS Text Size is not default, the Video Tab Bar PiP button will be resized accordingly"
            ]],
            ["1.11.0", "Added a new setting to make it possible for PiP to activate from either the video overlay button, the video tab bar button or dismissing the app at the same time"],
            ["1.10.1", "Possibly Fixed the tweak not working when PiP setting has never been on before"],
            ["1.10.0", "Updated for YTVideoOverlay 2.0.0"],
            ["1.9.0", [
                "Added YTVideoOverlay as a dependency, allowing you to make PiP button appear either top or bottom of the video overlay",
                "Made the tweak enabled by default",
                "Added th localization"
            ]],
            ["1.8.19", [
                "Fixed a possible crash on old YouTube versions when opening settings",
                "Added a localized version of tweak name for Polish"
            ]],
            ["1.8.17", [
                "Made tweak settings displayed without YouGroupSettings tweak (contributed by @dayanch96)",
                "Added pl localization"
            ]],
            ["1.8.16", [
                "Fixed the logic for adding PiP button to the video tab bar (contributed by NguyenASang)",
                "Added YouGroupSettings tweak as a dependency"
            ]],
            ["1.8.15", [
                "Updated setting icon",
                "Added id localization"
            ]],
            ["1.8.14", "Corrected detection of Module_Framework.framework"],
            ["1.8.12", "Corrected legacy PiP availability logic"],
            ["1.8.11", "Fixed crash on YouTube version 19.24.2 and higher"],
            ["1.8.10", "Optimized the hooks"],
            ["1.8.9 (16.29.4+)", [
                "Removed legacy code and files, minimum supported YouTube version is now 16.29.4",
                "Optimized the logic to add PiP button to the video tab bar"
            ]]
        ]
    },
    {
        "file": "youmusicpip",
        "title": "YouMusicPiP",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Enable native PiP in iOS YouTube Music app. This works for videos present in the app.</p>",
        "changes": [
            ["1.1.0", "Fixed support for modern app versions"]
        ]
    },
    {
        "file": "ytclassicvideoquality",
        "title": "YTClassicVideoQuality",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Revert to the original video quality selector in YouTube app.</p>",
        "changes": [
            ["1.4.0", "Use an alternative method to restore the video quality selector (contributed by @dayanch96)"],
            ["1.3.2", "Fixed crash on older YouTube versions"],
            ["1.3.1", "Fixed original video quality selector not showing on recent YouTube versions on iPhone devices"],
            ["1.2.0", "Added Premium formats to the classic video quality selector, if the video supports it"],
            ["1.1.0", "Use an alternative method to restore the video quality selector"],
            ["1.0.1", "Fixed crashing in YouTube version 16.20.5"]
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
            ["1.0.3", "Added support for YouTube version 19.47.7"],
            ["1.0.2", "Added support for YouTube version 16.45.4"]
        ]
    },
    {
        "file": "ytshortsprogress",
        "title": "YTShortsProgress",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Always enable progress bar and scrubbing in YouTube Shorts.</p>",
        "changes": [
            ["1.0.3", [  
                "Added more hooks (contributed by @dayanch96)",
                "Fixed a bug where swiping on a full-screen video always triggers progress bar change"
            ]]
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
            ["1.7.7", [
                "Translated the remaining languages using AI",
                "Added th localization"
            ]],
            ["1.7.6", "Made tweak settings displayed without YouGroupSettings tweak"],
            ["1.7.5", "Added YouGroupSettings tweak as a dependency"],
            ["1.7.4", [
                "Updated setting icon",
                "Added id localization"
            ]],
            ["1.7.3", [
                "Reduced hooks used for constructing tweak settings",
                "Updated vi localization"
            ]],
            ["1.7.2-1", [
                "Fixed crash when copying settings on YouTube version 19.13.1 and higher",
                "Updated tr localization"
            ]],
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
            ["1.5.1", "Fixed crash on YouTube version 19.03.2 and higher"],
            ["1.5.0-3", [
                "Tap on each A/B setting to reveal its class, copy it to clipboard or delete itself from the modified list",
                "Fixed \"View modified settings\" showing outdated settings",
                "Modified settings are now suffixed with \"*\"",
                "Search feature is now available only if grouped settings is disabled",
                "Confirmation alert will now show if you perform an action that requires quitting app",
                "Added support for YouTube version 16.42.3 and lower",
                "Added search functionality (contributed by @level3tjg)",
                "Added \"Group settings by prefixes\" option",
                "Optimized the existence check of modified settings",
                "Display \"Copied to clipboard\" alert also when modified settings are copied",
                "For long-named settings on iPhone, the non-truncated version will display",
                "Categorize feature flags into short prefixes for easier navigation",
                "Filtered out irrelevant features starting with amsterdam and unplugged",
                "Added settings from YTGlobalConfig class",
                "Breaking: Changed setting key format to \"YTABC.[Class].[Method]\" for future expansion but this also means you have to re-set your changes again",
                "Reduced memory footprint",
                "Added \"View modified settings\" and \"Copy current settings\" options"
            ]]
        ]
    },
    {
        "file": "ytmabconfig",
        "title": "YTMABConfig",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>YouTube Music usually implements a feature as an experiment. You may get to see it while others don't, and vice-versa.\
            This tweak adds a new section named \"A/B\" in the app settings where all features can be toggled freely by you.</p>",
        "changes": [
            ["1.0.2", "Removed debug code"],
            ["1.0.1", "Fixed crash when copying settings"]
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
                <li><a href=\"{}\">YTSystemAppearance</a></li>\
            </ul>".format(
                tweak_url("youarethere"),
                tweak_url("youremembercaption"),
                tweak_url("ytsystemappearance")
        ),
        "changes": [
            ["1.0.6", "Disabled the new floating mini-player style"],
            ["1.0.5", "Removed YTNoCheckLocalNetwork feature"],
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
            ["1.0.4", [
                "Added support for YouTube version 19.42.1",
                "Fixed possible crash in some cases (contributed by @bakedpotato191)"
            ]]
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
        "description": "<p>A helper tweak to add buttons on YouTube's video overlay.</p>",
        "changes": [
            ["2.1.1", "Ensure text overlay buttons are sized to be visible"],
            ["2.1.0", [
                "Added an ability to reorder the buttons",
                "Removed unnecessary YouQuality-specific code"
            ]],
            ["2.0.0", [
                "Simplified the code needed to add buttons to the video overlay from the tweak side",
                "Improved memory management"
            ]],
            ["1.3.0", [
                "Added +[YTSettingsSectionItemManager setTweak:hasOwnToggle:] method, for tweaks that have their own toggle",
                "Added tweak name above each button settings",
                "Added th localization",
                "Updated pl localization"
            ]],
            ["1.2.5", "Added default text style for text button"],
            ["1.2.4", "Added a localized version of tweak name for Polish"],
            ["1.2.3", "Made tweak settings displayed without YouGroupSettings tweak"],
            ["1.2.2", "Added YouGroupSettings tweak as a dependency"],
            ["1.2.1", [
                "Updated setting icon",
                "Added id localization"
            ]],
            ["1.2.0", "Added support for text button"],
            ["1.1.6", "Fixed the bottom buttons not showing on YouTube version 16.45.4 and lower"],
            ["1.1.5", "Fixed the bottom buttons not showing for some users"],
            ["1.1.4", "Fixed crash on YouTube version 19.03.2 and higher"],
            ["1.1.3", [
                "Increased the spacing between bottom buttons for better accessibility",
                "Fixed bottom buttons not positioned correctly on small iPhone devices",
            ]],
            ["1.1.2", "Fixed overlay buttons not appearing on YouTube version 19.02.1 and higher"],
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
            ["1.3.1", "Added th localization"],
            ["1.3.0", [
                "Updated for YTVideoOverlay 2.0.0",
                "If the video is muted then the user closes the video, the mute icon will update correctly when the user opens the video again"
            ]],
            ["1.2.4", [
                "Depends on YTVideoOverlay helper tweak",
                "Added setting page, allowing you to toggle tweak and change mute button position",
                "Fixed app crash on YouTube version 19.26.5 and higher",
                "Corrected mute button position when placed at the bottom and the audio track button is visible",
                "Added de, id, tr localization",
                "Added a localized version of tweak name for Polish"
            ]]
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
            ["1.3.5", "Depends on YTVideoOverlay 2.1.1+"],
            ["1.3.4", "Added th localization"],
            ["1.3.3", "Fixed 720p and lower quality text entering a new line when the button is placed at the top"],
            ["1.3.2", "Depends on YTVideoOverlay 2.1.0+"],
            ["1.3.1", "Removed unused code"],
            ["1.3.0", "Updated for YTVideoOverlay 2.0.0"],
            ["1.2.3", [
                "[Technical] On memory deallocation, only unregister its own observer",
                "Added ar, de, ja, pl, ru, tr, zh_cn localization",
                "Fixed quality label arrangement when the current video format has HDR",
                "Make label displays for non 60 FPS 720p, 1080p, 2K and 4K",
                "Depends on YTVideoOverlay helper tweak"
            ]]
        ]
    },
    {
        "file": "youspeed",
        "title": "YouSpeed",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Add a speed button to the video overlay where you can directly change the video speed.</p>",
        "changes": [
            ["1.1.3", [
                "Fixed vi localization not working",
                "Added th localization"
            ]],
            ["1.1.1", "Removed unused code"],
            ["1.1.0", "Updated for YTVideoOverlay 2.0.0"],
            ["1.0.1", [
                "[Technical] On memory deallocation, only unregister its own observer",
                "Added vi localization"
                "Initial release"
            ]]
        ]
    },
    {
        "file": "ytx",
        "title": "YouTube X",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>No ads and background playback for iOS YouTube app.</p>",
        "changes": [
            ["1.7.7", "Added background playback setting (under Offline)"],
            ["1.7.6", "Properly block shopping_item_card_list ads"],
            ["1.7.5", "Improved shorts ads blocking logic"],
            ["1.7.3", "Block shopping_carousel ads"],
            ["1.7.2", "Re-block search ads"],
            ["1.7.1", "Block new kind of video ads"],
            ["1.7.0", "Implement efficient feed ads blocking logic"],
            ["1.6.10", "Improved feed ads blocking logic"],
            ["1.6.8", "Hook YTAdShieldUtils class and Improve ads blocking logic"],
            ["1.6.6", "Improved feed ads blocking logic"],
            ["1.6.4", "Remove new format shorts ads"],
            ["1.6.3", [
                "Spoof YouTube version to 17.33.2 for clients with version as low as 16.29.4 to function properly"
                "Improved the performance of feed ads blocking",
                "Use an alternative way to hide statement_banner feed ads",
                "Use an alternative way to hide product_carousel feed ads",
                "Block feed ads by truly setting their size to zero",
                "Block YouTube upgrade dialog",
                "Switched to collection view hook, Block more kinds of feed ads"
            ]]
        ]
    },
    {
        "file": "youchoosequality",
        "title": "YouChooseQuality",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Auto-select the video quality of choice in iOS YouTube app.</p>",
        "changes": [
            ["1.0.5", "Moved the tweak description in the settings to under \"Enabled\" option so that the text is not cut off"],
            ["1.0.4", "Added th localization"],
            ["1.0.3", "Fixed incorrect resolution choosing when a video is vertical"],
            ["1.0.2", "Made tweak settings displayed without YouGroupSettings tweak"],
            ["1.0.1", "Added YouGroupSettings tweak as a dependency"],
            ["1.0.0-1", "Added vi, zh-Hans localization"]
        ]
    }
]
