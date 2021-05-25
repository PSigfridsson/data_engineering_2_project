$(document).ready(function(){

    $.getJSON("/_top10lang", function(data) {
        console.log(data);
        $('#top10lang').html(data);
    });

});