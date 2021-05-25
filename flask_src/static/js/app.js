$(document).ready(function(){

    $.getJSON("/_top10lang", function(data) {
        console.log(data.top10);
        $.each(data.top10, function(key,val) {
            console.log("Key: "+key+" - Val: "+val);
            $('#top10langtbody').append('<tr><td>'+key+'</td><td>'+val+'</td></tr>');
        });
    });

});