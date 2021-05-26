$(document).ready(function(){


    $("#top10langbutton").click(function() {
      topxLanguages(10);
    });

    $("#top10langbutton").click(function() {
      topxLanguages(15);
    });

    $("#top10langbutton").click(function() {
      topxLanguages(25);
    });

    $("#top10unittestbutton").click(function() {
      topxLanguages(10);
    });

    $("#top15unittestbutton").click(function() {
      topxLanguages(15);
    });

    $("#top25unittestbutton").click(function() {
      topxLanguages(25);
    });

});


function topxLanguages(x) {
    $.getJSON("/_topxlang", {'topx': x}, function(data) {
        $('#top10langtbody').html("");
        $.each(data.top10, function(key,val) {
            $('#top10langtbody').append('<tr><td>'+val[0]+'</td><td>'+val[1]+'</td></tr>');
        });
    });
}

function topxUnitTests(x) {
    $.getJSON("/_topxunittest", {'topx': x}, function(data) {
        $('#top10unittesttbody').html("");
        $.each(data.top10, function(key,val) {
            $('#top10unittesttbody').append('<tr><td>'+val[0]+'</td><td>'+val[1]+'</td></tr>');
        });
    });
}