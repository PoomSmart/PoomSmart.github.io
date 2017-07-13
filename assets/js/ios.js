var agent = navigator.userAgent;
var ios =  agent.match(/.*; CPU (?:iPhone )?OS ([0-9_]*) like Mac OS X[;)]/);
ios = ios == null ? '6.0' : ios[1].replace(/_/g,'.');
if (ios.match(/^[78910]($|\.)/) != null) {
  document.write('<link rel="stylesheet" type="text/css" href="../../assets/css/ios78.css"');
} else {
  document.write('<link rel="stylesheet" type="text/css" href="../../assets/css/legacy.css"');
}
