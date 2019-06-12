jQuery(document).ready(function ($) {
    function populateStars(current_rating) {
        $("#selected_rating").val(current_rating);
        $(".selected-rating").empty();
        $(".selected-rating").html(current_rating);

        if (current_rating == 0) {
           $('button[id^="rating-star"]').removeClass("btn-warning");
           $('button[id^="rating-star"]').addClass("btn-default");
        }

        for (i = 1; i <= current_rating; ++i) {
            $("#rating-star-" + i).toggleClass('btn-warning');
            $("#rating-star-" + i).toggleClass('btn-default');
        }
    }
    populateStars(Number($('input#loggedInUserRating').val()));

    function showError(message) {
        $("#message-display").text(message);
        $("#message-display").removeClass("hidden");
    }

    function hideError(message) {
        $("#message-display").addClass("hidden");
    }

    function addRating(value){
        var url = new URL(window.location.href);
        var userId = url.searchParams.get("userId");
        var productId = url.pathname.split('/')[3]
        $.ajax({
            type: "POST",
            url: "/casaone/ratings/v1/add",
            contentType: "application/json",
            data: JSON.stringify({rating: Number(value), userId: Number(userId), productId: Number(productId)}),
            success: function(data){
                if (data.status == "failure") {
                    showError(data.message);
                } else {
                    getDetailedRatings();
                    hideError();
                }
            }
        });
    }

    function removeRating(){
        var url = new URL(window.location.href);
        var userId = url.searchParams.get("userId");
        var productId = url.pathname.split('/')[3]
        $.ajax({
            type: "POST",
            url: "/casaone/ratings/v1/remove",
            contentType: "application/json",
            data: JSON.stringify({userId: Number(userId), productId: Number(productId)}),
            success: function(data){
                if (data.status == "failure") {
                    showError(data.message);
                } else {
                    getDetailedRatings();
                    populateStars(0);
                }
            }
        });
    }

    function getDetailedRatings(){
        var url = new URL(window.location.href);
        var userId = url.searchParams.get("userId");
        var productId = url.pathname.split('/')[3]
        $.ajax({
            type: "POST",
            url: "/casaone/ratings/v1/getDetailed",
            contentType: "application/json",
            data: JSON.stringify({userId: Number(userId), productId: Number(productId)}),
            success: function(data){
                repaintRatingWidget(data.data);
            }
        });
    }

    function repaintRatingWidget(data){
        $("#total-ratings").text(data.totalRatings + " Total Ratings");
        $("#average-rating").text(data.averageRating);
        $("#5-star-bar").css('width', (data.ratingsBreakdown["5"]).toString() + "%");
        $("#4-star-bar").css('width', (data.ratingsBreakdown["4"]).toString() + "%");
        $("#3-star-bar").css('width', (data.ratingsBreakdown["3"]).toString() + "%");
        $("#2-star-bar").css('width', (data.ratingsBreakdown["2"]).toString() + "%");
        $("#1-star-bar").css('width', (data.ratingsBreakdown["1"]).toString() + "%");
        $("#5-star-text").text((data.ratingsBreakdown["5"]).toString() + "%");
        $("#4-star-text").text((data.ratingsBreakdown["4"]).toString() + "%");
        $("#3-star-text").text((data.ratingsBreakdown["3"]).toString() + "%");
        $("#2-star-text").text((data.ratingsBreakdown["2"]).toString() + "%");
        $("#1-star-text").text((data.ratingsBreakdown["1"]).toString() + "%");
    }


	$(".btnrating").on('click', (function (e) {

		var previous_value = $("#selected_rating").val();

		var selected_value = $(this).attr("data-attr");
		$("#selected_rating").val(selected_value);

		$(".selected-rating").empty();
		$(".selected-rating").html(selected_value);

		for (i = 1; i <= selected_value; ++i) {
			$("#rating-star-" + i).toggleClass('btn-warning');
			$("#rating-star-" + i).toggleClass('btn-default');
		}

		for (ix = 1; ix <= previous_value; ++ix) {
			$("#rating-star-" + ix).toggleClass('btn-warning');
			$("#rating-star-" + ix).toggleClass('btn-default');
		}

        if (previous_value != selected_value) {
            addRating(selected_value);
        }
	}));

	$("#remove-rating").on('click', (function (e) {
	    removeRating();
	}));

});