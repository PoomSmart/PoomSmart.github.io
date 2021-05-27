/*! Basic iOS 7 CSS // Apache License 2.0 // hbang.ws */
!function(e){"use strict";var i,t=e.documentElement,d=t.classList;-1!=navigator.userAgent.indexOf("Cydia")?(-1!=e.title.indexOf(" · ")&&(e.title=e.title.split(" · ")[0]),d.add("cydia")):d.remove("cydia","depiction"),"devicePixelRatio"in window&&2<=devicePixelRatio&&((i=e.createElement("div")).style.border=".5px solid transparent",t.appendChild(i),0<i.offsetHeight&&d.add("has-subpixel"),3<=devicePixelRatio&&d.add("has-subpixel-3x"),t.removeChild(i))}(document);
//# sourceMappingURL=ios7.min.js.map
