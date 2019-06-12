jQuery(document).ready(function ($) {
    var current_rating = Number($('input#loggedInUserRating').val())
    $("#selected_rating").val(current_rating);
	$(".selected-rating").empty();
	$(".selected-rating").html(current_rating);

    for (i = 1; i <= current_rating; ++i) {
        $("#rating-star-" + i).toggleClass('btn-warning');
        $("#rating-star-" + i).toggleClass('btn-default');
	}


    function addRating(value){
        var url = new URL(window.location.href);
        var userId = url.searchParams.get("userId");
        var productId = url.pathname.split('/')[2]
        $.ajax({
            type: "POST",
            url: "/ratings/v1/add",
            contentType: "application/json",
            data: JSON.stringify({rating: Number(value), userId: Number(userId), productId: Number(productId)}),
            success: function(data){
                console.log(data)
            }
        });
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
            addRating(selected_value)
        }
	}));

});