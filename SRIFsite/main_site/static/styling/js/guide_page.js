$(function() {
	$(".method:first-of-type").click(function() {
		$("#hide2").removeClass("expanded");
		$("#hide3").removeClass("expanded");
		$("#hide1").toggleClass("expanded");
		$(".method:nth-of-type(3)").removeClass("green_highlight");
		$(".method:nth-of-type(2)").removeClass("green_highlight");
		$(".wrapper > .method:first-of-type").toggleClass("green_highlight");
	
	});
});
$(function() {
	$(".method:nth-of-type(2)").click(function() {
		$("#hide1").removeClass("expanded");
		$("#hide3").removeClass("expanded");
		$("#hide2").toggleClass("expanded");
		$(".method:nth-of-type(3)").removeClass("green_highlight");
		$(".method:first-of-type").removeClass("green_highlight");
		$(".method:nth-of-type(2)").toggleClass("green_highlight");

	});
});
$(function() {
	$(".method:nth-of-type(3)").click(function() {
		$("#hide2").removeClass("expanded");
		$("#hide1").removeClass("expanded");
		$("#hide3").toggleClass("expanded");
		$(".method:first-of-type").removeClass("green_highlight");
		$(".method:nth-of-type(2)").removeClass("green_highlight");
		$(".method:nth-of-type(3)").toggleClass("green_highlight");

	});
});