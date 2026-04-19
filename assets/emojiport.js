(function () {
    const iosSelect = document.getElementById("ios");
    const deviceSelect = document.getElementById("device");
    const output = document.getElementById("emojifontpath");

    if (!iosSelect || !deviceSelect || !output) {
        return;
    }

    function getEmojiFontPath() {
        const ios = Number(iosSelect.value);
        const device = Number(deviceSelect.value);

        if (!ios || !device) {
            output.value = "Path will be displayed here";
            return;
        }

        let path;
        let name;

        switch (ios) {
            case 1:
                path = "/System/Library/Fonts/Cache";
                if (device === 3) {
                    name = "AppleColorEmoji@2x.ttf";
                } else if (device !== 1) {
                    name = "AppleColorEmoji.ttf";
                }
                break;
            case 2:
                path = "/System/Library/Fonts/Core";
                if (device === 3) {
                    name = "AppleColorEmoji_2x.ttf";
                } else if (device !== 1) {
                    name = "AppleColorEmoji_1x.ttf";
                }
                break;
            case 3:
                path = "/System/Library/Fonts/Core";
                name = device === 2 ? "AppleColorEmoji.ttf" : "AppleColorEmoji@2x.ttf";
                break;
            case 4:
                path = "/System/Library/Fonts/Core";
                name = device === 3 ? "AppleColorEmoji@2x.ttc" : "AppleColorEmoji.ttc";
                break;
            case 5:
                path = device === 1 ? "/System/Library/Fonts/Core" : "/System/Library/Fonts/CoreAddition";
                if (device === 1) {
                    name = "AppleColorEmoji.ttc";
                } else if (device === 3) {
                    name = "AppleColorEmoji-160px.ttc";
                }
                break;
            default:
                break;
        }

        output.value = path && name ? path + "/" + name : "Not applicable";
    }

    iosSelect.addEventListener("change", getEmojiFontPath);
    deviceSelect.addEventListener("change", getEmojiFontPath);
})();