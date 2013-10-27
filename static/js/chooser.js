$(document).ready(function() {
	$("#Go").click(function() {
		var qualityMode =""
		// get selected		
		$("a").each(function(){
	     		if($(this).attr("href") == "#selected"){
				qualityMode = $(this).text();	
				
		}});
		

		// build Link
		var link = "/channel?channel=" + $("#selecting option:selected").val() + "&quality=" + $.trim(qualityMode);
		window.location = link;
		
	});

	$("#fullQuality").click(function() {
		$("#fullQuality").attr("href", "#selected");
		$("#fullQuality").css("font-weight", "bold");
		$("#limitedQuality").css("font-weight", "normal");
		$("#limitedQuality").attr("href", "");
		
	});

	$("#limitedQuality").click(function() {
		$("#limitedQuality").attr("href", "#selected");
		$("#limitedQuality").css("font-weight", "bold");
		$("#fullQuality").css("font-weight", "normal");
		$("#fullQuality").attr("href", "");
	});



    });