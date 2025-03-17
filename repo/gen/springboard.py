springboard = [
    {
        "file": "cconoff",
        "title": "CC On & Off",
        "min_ios": "11.0",
        "description": "<p>Toggles Wi-Fi and Bluetooth On/Off explicitly from Control Center on iOS 11+.</p>",
        "changes": [
            ["1.1.0", "Fixed Bluetooth not turning off on iOS 15"],
            ["1.0.0", "Compiled with ARC"]
        ]
    },
    {
        "file": "blurrybadges",
        "title": "Blurry Badges",
        "min_ios": "13.0",
        "description": "<p>Adds colored blur to SpringBoard icon badges.</p>",
        "changes": [
            ["1.5.3", "Added support for iOS 13"],
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
        "file": "nottodayhomescreensidebar",
        "title": "NotTodayHomeScreenSideBar",
        "min_ios": "14.0",
        "max_ios": "14.8.1",
        "strict_range": True,
        "screenshots": True,
        "featured_as_banner": True,
        "inline_source_code": True,
        "description": "<p>Prevents Today View sidebar from being pinned on iPad homescreen. Widgets in Today View will still be accessible by swiping to the leftmost of the homescreen, just like how it is on iPad portrait or iPhone.</p>"
    },
    {
        "file": "expandedclassicscreen",
        "title": "expandedclassicscreen",
        "min_ios": "14.0",
        "screenshots": True,
        "inline_source_code": True,
        "description": "<p>Uses a larger 414x736 (iPhone 6s+) resolution for classic apps on iPad.</p>"
    },
    {
        "file": "anywherewidgetsforipad",
        "title": "Anywhere Widgets for iPad",
        "min_ios": "14.0",
        "max_ios": "14.8.1",
        "strict_range": True,
        "featured_as_banner": True,
        "description": "<p>Allows widgets to be on home screen on iPad.</p>",
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
        "file": "padgrid",
        "title": "PadGrid",
        "min_ios": "7.0",
        "description": "<p>Increases home screen icon grid size for iPad.</p>",
        "changes": [
            ["1.2.0", "Added Reduce edge insets option for iPadOS 15+"],
            ["1.1.2", "Made IconOrder an option for icon layout persistence library"],
            ["1.1.1", "Added folder rows and columns settings (iOS 14+, contributed by @UInt2048)"]
        ]
    },
]
