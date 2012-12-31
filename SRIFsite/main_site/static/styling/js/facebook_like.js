// Javascript to get our facebook liking to sync to this page; 
// without this the like box won't show up on bottom of page

$(function(){
	console.log("hi");
	$('ul a').bind('click',function(event){
		var $anchor = $(this);

		$('html, body').stop().animate({
			scrollTop: $($anchor.attr('href')).offset().top
		}, 1000,'easeOutExpo');

		event.preventDefault();
	
	});
});
