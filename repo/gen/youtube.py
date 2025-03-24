from helper import *

youtube = [
    {
        "file": "ytuhd",
        "title": "YTUHD",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Unlocks 1440p and 2160p resolutions (VP9-compatible) in iOS YouTube app.</p>",
        "changes": [
            ["1.6.0", [
                "Added some libvpx settings that you can configure for VP9 decoding behavior, mainly setting the number of decoding threads"
            ]],
            ["1.5.11", [
                "\"Use VP9\" setting is no longer enabled by default",
                "Removed the hooks to fall back to use the old ABR policy"
            ]],
            ["1.5.10", [
                "In settings, corrected the minimum hardware VP9 device requirement from A11 to A12",
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
                "Force VP9 formats only for 1440p and higher",
                "Added \"VP9 for all\" option where you can enable VP9 for all resolutions",
                "Fixed crash on YouTube version 19.03.2 and higher",
                "Updated spoof version to 15.8.1 (for iOS 14-)",
                "Hooks MLABRPolicyNew and MLABRPolicyOld classes (introduced in YouTube version 17.30.3)",
                "Fixed crashing on some older YouTube versions",
                "Forces enabling Video quality settings on older YouTube to have YTUHD setting there",
                "Added th localization",
                "Updated es, zh_cn localization"
            ]]
        ]
    },
    {
        "file": "youpip",
        "title": "YouPiP",
        "min_ios": "11.0",
        "tintColor": "red",
        "featured_as_banner": True,
        "description": "<p>Enables native PiP in iOS YouTube app.</p>\
            <p>YouPiP best supports the latest version of YouTube. You may downgrade to as far as version 16.29.4, older versions will not be (fully) supported.</p>",
        "changes": [
            ["1.12.7", "PiP should no longer activate if either \"Use PiP Button\" or \"Use Video Tab Bar Button\" is enabled"],
            ["1.12.6", "PiP should no longer activate if the YouTube's own PiP setting is off"],
            ["1.12.5", [
                "Fixed PiP not working on iOS 13",
                "Removed Legacy PiP option from iOS 13, because it must be enabled regardless",
                "Known issue (iOS 13): PiP may not activate if it is not activated from the PiP button",
                "Depends on ForceInPicture 1.0.1+ for iPhones running iOS 13 and lower",
                "Fixed appWillEnterBackground: method not being called on iOS 14"
            ]],
            ["1.12.4", "Added missing hooks for Legacy PiP for recent YouTube versions"],
            ["1.12.3", "Background playback is no longer forcibly enabled for YouPiP, you should ensure it is enabled in the original YouTube app settings"],
            ["1.12.2", [
                "Simplified PiP enabling logic",
                "Fixed setting icon not appearing when the tweak is disabled and grouped settings experiment is on",
                "Fixed the tweak setting icon and Video Tab Bar PiP button being black in dark mode on YouTube version 20.02.3",
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
            ["1.8.19 (16.29.4+)", [
                "Removed legacy code and files, minimum supported YouTube version is now 16.29.4",
                "Added YouGroupSettings tweak as an optional dependency",
                "Fixed the logic for adding PiP button to the video tab bar (contributed by NguyenASang)",
                "Fixed crash on YouTube version 19.24.2 and higher",
                "Fixed a possible crash on old YouTube versions when opening settings",
                "Corrected Legacy PiP availability logic",
                "Corrected detection of Module_Framework.framework",
                "Optimized the logic to add PiP button to the video tab bar",
                "Added a localized version of tweak name for Polish",
                "Added id, pl localization"
            ]]
        ]
    },
    {
        "file": "youmusicpip",
        "title": "YouMusicPiP",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Enables native PiP in iOS YouTube Music app. This works for videos present in the app.</p>",
        "changes": [
            ["1.1.0", "Fixed support for modern app versions"]
        ]
    },
    {
        "file": "ytclassicvideoquality",
        "title": "YTClassicVideoQuality",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Reverts to the original video quality selector in YouTube app.</p>",
        "changes": [
            ["1.5.1", "Fixed incorrect video quality list position on iPad"],
            ["1.5.0", "Fixed the tweak not working inside video premium controls"],
            ["1.4.0", "Used an alternative method to restore the video quality selector (contributed by @dayanch96)"],
            ["1.3.2", "Fixed crash on older YouTube versions"],
            ["1.3.1", "Fixed original video quality selector not showing on recent YouTube versions on iPhone devices"],
            ["1.2.0", "Added Premium formats to the classic video quality selector, if the video supports it"],
            ["1.1.0", "Used an alternative method to restore the video quality selector"],
            ["1.0.1", "Fixed crashing in YouTube version 16.20.5"]
        ]
    },
    {
        "file": "ytsystemappearance",
        "title": "YTSystemAppearance",
        "min_ios": "13.0",
        "tintColor": "red",
        "inline_source_code": True,
        "description": "<p>Enables setting appearance (Light/Dark) based on system in YouTube app. Because this feature is based on iOS dark mode, the tweak only supports iOS/iPadOS 13 and above. YouTube version 15.10.4 and higher are officially supported. Older (but not too old) versions may.</p>"
    },
    {
        "file": "ytreexplore",
        "title": "YTReExplore",
        "min_ios": "11.0",
        "tintColor": "red",
        "screenshots": True,
        "description": "<p>Removes Shorts tab and replace with Explore tab in YouTube app.</p>\
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
        "description": "<p>Always enables progress bar and scrubbing in YouTube Shorts.</p>",
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
        "description": "<p>Disables \"Video paused. Continue watching?\" popup in YouTube app when you play a long video.</p>"
    },
    {
        "file": "noytpremium",
        "title": "NoYTPremium",
        "min_ios": "11.0",
        "tintColor": "red",
        "inline_source_code": True,
        "description": "<p>Removes YouTube Premium upsells.</p>"
    },
    {
        "file": "noytmpremium",
        "title": "NoYTMPremium",
        "min_ios": "11.0",
        "tintColor": "red",
        "inline_source_code": True,
        "description": "<p>Removes YouTube Music Premium upsell elements (banner, alerts, tab item).</p>"
    },
    {
        "file": "youremembercaption",
        "title": "YouRememberCaption",
        "min_ios": "11.0",
        "tintColor": "red",
        "inline_source_code": True,
        "description": "<p>Makes YouTube remember your video caption setting, if not already.</p>"
    },
    {
        "file": "ytnochecklocalnetwork",
        "title": "YTNoCheckLocalNetwork",
        "min_ios": "11.0",
        "tintColor": "red",
        "inline_source_code": True,
        "screenshots": True,
        "description": "<p>Removes Local Network permission check in YouTube app.</p>"
    },
    {
        "file": "ytnopaidpromo",
        "title": "YTNoPaidPromo",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Removes \"Include paid promotion\" banner from videos on YouTube app.\
            <a target=\"_blank\" href=\"https://www.youtube.com/watch?v=FxyW7Gp9Jd4\">What is paid promotion?</a></p>"
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
            ["1.7.8", "Removed kidsClient* and musicOfflineClient* A/B flags as they are unrelated to YouTube app"],
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
            ["1.6.0", "You can now import the YTABConfig settings from the clipboard"]
        ]
    },
    {
        "file": "ytabconfigreset",
        "title": "YTABConfigReset",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Resets all A/B flags in YTABConfig tweak on YouTube app launch. This is useful when changing some A/B flags may cause the app to crash outright and there is no simple way to recover it. Once installed and you launched the YouTube app, all A/B flags will be reset. You will then uninstall YTABConfigReset tweak. Otherwise, A/B flags will keep being reset every time you launch the app.</p>"
    },
    {
        "file": "ytmabconfig",
        "title": "YTMABConfig",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>YouTube Music usually implements a feature as an experiment. You may get to see it while others don't, and vice-versa.\
            This tweak adds a new section named \"A/B\" in the app settings where all features can be toggled freely by you.</p>",
        "changes": [
            ["1.0.3", [
                "Removed \"shorts\" settings because they are irrelevant for YouTube Music",
                "Added id, th localization"
            ]],
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
                <li><a target=\"_blank\" href=\"{}\">YouAreThere</a></li>\
                <li><a target=\"_blank\" href=\"{}\">YouRememberCaption</a></li>\
                <li><a target=\"_blank\" href=\"{}\">YTSystemAppearance</a></li>\
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
        "description": "<p>Makes your video full-screen on playing.</p>",
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
        "description": "<p>Removes popup when you like/dislike videos; those saying you liked the video and feedback shared with the creator.</p>"
    },
    {
        "file": "ytvideooverlay",
        "title": "YTVideoOverlay",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>A helper tweak to add buttons on YouTube's video overlay.</p>",
        "changes": [
            ["2.2.2", "Fixed bottom buttons being too far apart from each other on YouTube version 20.12.4"],
            ["2.2.1", "Fixed incorrect button position in full-screen mode on recent YouTube versions"],
            ["2.2.0", "Added support for extra boolean settings from the tweak side"],
            ["2.1.2", [
                "Fixed button order not visually changing in the settings",
                "Translated the remaining languages using AI"
            ]],
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
                "Added support for text button",
                "Updated setting icon",
                "Fixed the bottom buttons not showing on YouTube version 16.45.4 and lower",
                "Fixed the bottom buttons not showing for some users",
                "Fixed crash on YouTube version 19.03.2 and higher",
                "Fixed bottom buttons not positioned correctly on small iPhone devices",
                "Fixed overlay buttons not appearing on YouTube version 19.02.1 and higher",
                "Fixed incorrect button positioning in some scenarios",
                "Added de, id localization",
                "Updated ja localization",
                "Increased the spacing between bottom buttons for better accessibility"
            ]]
        ]
    },
    {
        "file": "youmute",
        "title": "YouMute",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Adds a mute button to the video overlay where you can directly mute or unmute the video.</p>",
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
        "description": "<p>Adds a video quality to the video overlay where you can easily change the video quality.</p>\
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
        "description": "<p>Adds a speed button to the video overlay where you can directly change the video speed. Also add more video speeds to choose from.</p>",
        "changes": [
            ["1.3.0", "Added the ability to replace the default video speed selector with the primitive one, where custom speeds can be added"],
            ["1.2.1", "Fixed video speed button not updating when changing the video speed on old YouTube versions"],
            ["1.2.0", "Added more video speeds to choose from, configured from YTVideoOverlay settings"],
            ["1.1.3", [
                "Fixed vi localization not working",
                "Added th localization"
            ]],
            ["1.1.1", "Removed unused code"],
            ["1.1.0", "Updated for YTVideoOverlay 2.0.0"],
            ["1.0.1", [
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
        "description": "<p>No ads, background playback and legacy compatibility for iOS YouTube app.</p>",
        "changes": [
            ["1.7.12", "Made YouTube version 17.x.x/18.x.x functional again"],
            ["1.7.11", "Fixed video comments section not loading on old YouTube versions"],
            ["1.7.10", "Blocked in-video product ads overlay and engagement panel"],
            ["1.7.9", "Fixed shorts ads blocking on YouTube version 20.06.3 and higher"],
            ["1.7.8", "Fixed shorts ads blocking on old YouTube versions"],
            ["1.7.7", "Added background playback setting (under Offline)"],
            ["1.7.6", "Properly blocked shopping_item_card_list ads"],
            ["1.7.5", "Improved shorts ads blocking logic"],
            ["1.7.3", "Blocked shopping_carousel ads"],
            ["1.7.2", "Re-blocked search ads"],
            ["1.7.1", "Blocked new kind of video ads"],
            ["1.7.0", "Implemented efficient feed ads blocking logic"],
            ["1.6.10", [
                "Spoofed YouTube version to 17.33.2 for clients with version as low as 16.29.4 to function properly",
                "Improved feed ads blocking logic",
                "Improved the performance of feed ads blocking",
                "Removed new format shorts ads",
                "Hooked YTAdShieldUtils class",
                "Used an alternative way to hide statement_banner feed ads",
                "Used an alternative way to hide product_carousel feed ads",
                "Blocked feed ads by truly setting their size to zero",
                "Blocked YouTube upgrade dialog",
                "Switched to collection view hook, Block more kinds of feed ads"
            ]]
        ]
    },
    {
        "file": "youchoosequality",
        "title": "YouChooseQuality",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Auto-selects the video quality of choice in iOS YouTube app.</p>",
        "changes": [
            ["1.0.6", "Shortened each scenario label in settings so that devices of a small form factor can see the full text"],
            ["1.0.5", "Moved the tweak description in the settings to under \"Enabled\" option so that the text is not cut off"],
            ["1.0.4", "Added th localization"],
            ["1.0.3", "Fixed incorrect resolution choosing when a video is vertical"],
            ["1.0.2", "Made tweak settings displayed without YouGroupSettings tweak"],
            ["1.0.1", "Added YouGroupSettings tweak as a dependency"]
        ]
    },
    {
        "file": "youslider",
        "title": "YouSlider",
        "min_ios": "13.0",
        "tintColor": "red",
        "description": "<p>Customizes YouTube video slider and scrubber color. You can also replace the scrubber with your own image.</p>",
        "changes": [
            ["1.1.1", "Fixed app crash on older 19.x YouTube versions"],
            ["1.1.0", [
                "Fixed scrubber sizing logic in regular videos",
                "Fixed scrubber styling when the scrubber size is non-default",
                "Added 55% - 200% scrubber size options",
                "Applied slider and scrubber customization to auto-playing videos in the home page"
            ]]
        ]
    },
    {
        "file": "ytlegacy",
        "title": "YouTube Legacy",
        "min_ios": "11.0",
        "tintColor": "red",
        "description": "<p>Attempts to make old YouTube versions functional and not crash as the time goes by.</p>"
    }
]
