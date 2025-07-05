app = [
    {
        "file": "githubweblegacycompat",
        "title": "GitHubWebLegacyCompat",
        "min_ios": "8.0",
        "max_ios": "16.3.1",
        "description": "<p>Makes GitHub website more accessible on iOS 16.3 and lower by injecting JS and CSS with unsupported syntax removed.</p>",
        "changes": [
            ["2.3.5", "Updated JS for the recent GitHub changes"],
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
            ["1.3.2", "Fixed UI layout on iOS 15.0 - 15.3"],
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
            ["2.8.1", "Spoofed iOS version to 16.3 for devices running under iOS 16.3"],
            ["2.8.0", [
                "Added support for extended ISO 8601 date format (< 16.0)",
                "Removed `max-width: 100% from viewport CSS workaround",
            ]],
            ["2.7.0", [
                "Added polyfill for String.matchAll (< 13.0)",
                "Added polyfill for globalThis (< 12.1)",
                "Added polyfill for Reflect (< 10.0)"
            ]],
            ["2.6.0", [
                "Added polyfill for structuredClone (< 15.4)",
                "Added polyfill for Object.getOwnPropertyDescriptors, String.padStart and String.padEnd (< 10.0)",
                "Added polyfill for Number.{EPSILON,MAX_SAFE_INTEGER,MIN_SAFE_INTEGER,NEGATIVE_INFINITY,POSITIVE_INFINITY}. Number.isInteger and Number.isSafeInteger (< 9.0)"
            ]],
            ["2.5.0", [
                "Included iOS 15.2 - 15.3 for viewport CSS workaround",
                "Made viewport CSS workaround apply to only mobile devices",
                "Added polyfills for Array.flat, String.trimStart, String.trimEnd and Symbol.description (< 12.0)",
                "Added polyfill for Promise.finally (< 11.1)",
                "Simplified NodeList.forEach polyfill (< 10.0)"
            ]],
            ["2.4.0", [
                "Added polyfill for RegExp.escape (< 18.2)",
                "Added polyfills for Array.toSorted, Array.toSpliced and Array.with (< 16.0)",
                "Added polyfill for Promise.any (< 14.0)",
                "Added polyfill for Object.fromEntries (< 12.1)",
                "Fixed Element.matches compatibility workaround still not working correctly (< 15.6)",
                "Included iOS 15.0 - 15.1 for viewport CSS workaround"
            ]],
            ["2.3.1", "Added RegExp Lookbehind (Polyfills) tweak as a dependency"],
            ["2.3.0", [
                "Removed RegExp lookbehind polyfill as it is now part of a separate package RegExp Lookbehind (Polyfills)",
                "Added polyfill for dynamic import (< 15.2)",
                "Added polyfill for Object.getOwnPropertySymbols (< 9.0)"
            ]],
            ["2.2.3", "Fixed app crash due to problematic RegExp (< 16.4)"],
            ["2.2.2", "Fixed RegExp lookbehind polyfill breaking some websites (< 16.4)"],
            ["2.2.1", "Improved RegExp lookbehind polyfill (< 16.4)"],
            ["2.2.0", [
                "Made CSS Cascade layers workaround work for dynamically added stylesheets",
                "Added polyfill for EventTarget (< 14.0)",
                "Readded viewport CSS workaround (< 15.0)",
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
                "Spoofed iOS version to 16.0 for devices running under iOS 16.0",
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
                "Removed problematic viewport CSS workaround"
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
                "Added viewport CSS workaround to fix incomplete page width on iOS 14 and lower"
            ]],
        ]
    },
    {
        "file": "polyfillsregexplookbehind",
        "title": "RegExp Lookbehind (Polyfills)",
        "description": "<p>Provides a polyfill for RegExp lookbehind feature that is not available on iOS 16.4 and lower.</p>",
        "changes": [
            ["1.2.2", "Fixed polyfill compatibility on some websites"],
            ["1.2.1", "Added regex replacement mechanism so that complex regexes are transformed to simpler ones without lookbehind"],
            ["1.1.2", "Fixed the polyfill crashing in some scenarios"],
            ["1.1.0", "Rewrote the polyfill"],
            ["1.0.1", "Fixed the polyfill crashing in some scenarios"],
        ]
    },
    {
        "file": "steamweblegacycompat",
        "title": "SteamWebLegacyCompat",
        "min_ios": "14.1",
        "max_ios": "16.3.1",
        "description": "<p>Makes Steam website more accessible on iOS 16.3 and lower by injecting JS with unsupported syntax removed.</p>"
    }
]