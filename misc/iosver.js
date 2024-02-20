const VERSION_CHECK_SUPPORTED = "Your iOS version is supported! &#x1f60a;";
const VERSION_CHECK_UNCONFIRMED = "Not yet tested on iOS %s &#x1f601;";

(function (document) {
	"use strict";

	if (navigator.userAgent.indexOf("Dark") != -1) {
		document.body.setAttribute("data-theme", "dark");
	}

	function setMessage(m) {
		document.getElementById("pt").innerHTML += "<br/>" + m;
	}

	function toNum(bits) {
		return (10000 * parseInt(bits[0])) + parseInt((100 * (bits[1] ? bits[1] : 0))) + parseInt(bits[2] ? bits[2] : 0);
	}

	function parseVersionString(version) {
		var bits = version.split(".");
		return toNum(bits);
	}

	function compareVersions(one, two) {
		var two_ = toNum(two);
		return one != two_ ? (one > two_ ? 1 : -1) : 0;
	}

	var prerequisite = document.getElementById("prerequisite");
	var version = navigator.appVersion.match(/CPU( iPhone)? OS (\d+)_(\d+)(_(\d+))? like/i);

	if (!prerequisite) {
		return;
	}

	if (!version && navigator.maxTouchPoints > 0 && navigator.appVersion.indexOf("(Macintosh; Intel Mac OS X 10_15") !== -1) {
		version = navigator.appVersion.match(/(Version)\/(\d+)\.(\d+)(\.(\d+))?/i);
	}

	var minString = prerequisite.dataset.minIos;
	var maxString = prerequisite.dataset.maxIos;

	var minVersion = parseVersionString(minString);
	var maxVersion = maxString ? parseVersionString(maxString) : null;
	var message = null;

	if (version) {
		var osVersion = [version[2], version[3], version[4] ? version[5] : 0];
		var osString = osVersion[0] + "." + osVersion[1] + (osVersion[2] && osVersion[2] != 0 ? "." + osVersion[2] : "");
		message = VERSION_CHECK_SUPPORTED;
		if (compareVersions(minVersion, osVersion) == 1) {
			message = null;
		} else if (maxVersion && compareVersions(maxVersion, osVersion) == -1) {
			if ("unsupported" in prerequisite.dataset) {
				message = null;
			} else {
				message = VERSION_CHECK_UNCONFIRMED.replace("%s", osString);
			}
		}
		if (message)
			setMessage(message);
	}
})(document);
