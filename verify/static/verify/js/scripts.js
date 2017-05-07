
if (/Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent)) {
	$('#backplate').height($(window).height() - 10);
} else {
	$('#backplate').height($(window).height() - 100);
}



// // on successful verification
// $("body").animate({
// 	backgroundColor: "#20FFAD"
// }, 1500);
//
// $("#message").css("color", "#20FFAD");
// document.getElementById("message").innerHTML = "Verification Successful";

// on failed verification
$("body").animate({
	backgroundColor: "#f5003c"
}, 1500);
$("#message").css("color", "#f5003c");
document.getElementById("message").innerHTML = "Verification Failed";
