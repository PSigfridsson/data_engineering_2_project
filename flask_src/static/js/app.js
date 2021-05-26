$(document).ready(function(){


    $("#top10langbutton").click(function() {
      topxLanguages(10);
    });

});


function topxLanguages(x) {
    $.getJSON("/_topxlang", {'topx': x}, function(data) {
        console.log(data.top10);
        $.each(data.top10, function(key,val) {
            console.log("Val0: "+val[0]+" - Val1: "+val[1]);
            $('#top10langtbody').append('<tr><td>'+val[0]+'</td><td>'+val[1]+'</td></tr>');
        });
    });
}

function topxUnitTests(x) {
    $.getJSON("/_topxunittest", {'topx': x}, function(data) {
        console.log(data.top10);
        $.each(data.top10, function(key,val) {
            console.log("Val0: "+val[0]+" - Val1: "+val[1]);
            $('#top10unittesttbody').append('<tr><td>'+val[0]+'</td><td>'+val[1]+'</td></tr>');
        });
    });
}