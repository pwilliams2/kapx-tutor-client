/**
 * Created by admin on 1/27/15.
 */

//var hangoutsBaseUrl = "https://plus.google.com/hangouts/_/";
var hangoutsBaseUrl = "https://talkgadget.google.com/hangouts/_/"  //gid is appended below at run-time

function launchClientHangout(gid) {
    var url = hangoutsBaseUrl + gid + "?gd=s";
    window.open(url, "", "width=1002,height=700,location=0,menubar=0,scrollbars=1,status=1,resizable=0")
}

$(".launch-hangout").click(function () {
    gid = $(this).find(".gid").text();
    console.log("gid: " + gid);
    launchClientHangout(gid);
});

function reload() {
    window.location.reload();
};
$(function () { //reload page 20 seconds
    setInterval(function () {
        reload();
    }, 20000);
});

