$("#maxima_submit").click(function(){
    $.ajax({
        type: "POST",
        url: "cgi-bin/webmaxima.cgi",
        data: {maxima_input: $("#maxima_input").val()},
        error: function(result) {
        },
        success: function(result) {
            $("#maxima_output").val(result);
        }
    });
});
