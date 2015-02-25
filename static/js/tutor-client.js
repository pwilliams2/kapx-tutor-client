/**
 * Created by admin on 1/27/15.
 */

//var hangoutsBaseUrl = "https://talkgadget.google.com/hangouts/_/"  //gid is appended below at run-time
//function launchClientHangout(gid, subject) {
//    var url = hangoutsBaseUrl + gid + '?gd=' + subject;
//    console.log('url: ' + url);
//    window.open(url, "", "width=1002,height=700,location=0,menubar=0,scrollbars=1,status=1,resizable=0")
//}

function launchClientHangout(gid, subject) {
    var url = "https://kx-tutor-hangout-app.appspot.com/hangouts?gid=" + gid + '&subject=' + subject;
    console.log('url: ' + url);
    window.open(url, "", "width=1002,height=700,location=0,menubar=0,scrollbars=1,status=1,resizable=0")
}

$(".launch-hangout").click(function () {
    gid = $(this).find(".gid").text();
    subject = $(this).find(".subject").text();
    launchClientHangout(gid, subject);
});

function reload() {
    window.location.reload();
};
$(function () { //reload page 20 seconds
    setInterval(function () {
        reload();
    }, 60000);
});

