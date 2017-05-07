
if (/Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent)) {
	$('#backplate').height($(window).height() - 10);
} else {
	$('#backplate').height($(window).height() - 100);
}
