$(document).ready(function(){

    // Top languages
    $("#top10langbutton").click(function() {
      topxLanguages(10);
    });

    $("#top15langbutton").click(function() {
      topxLanguages(15);
    });

    $("#top25langbutton").click(function() {
      topxLanguages(25);
    });

    // Top commited repos
    $("#top10commitbutton").click(function() {
      topxCommitedRepos(10);
    });

    $("#top15commitbutton").click(function() {
      topxCommitedRepos(15);
    });

    $("#top25commitbutton").click(function() {
      topxCommitedRepos(25);
    });

    // Top languages with unittests
    $("#top10unittestbutton").click(function() {
      topxUnitTests(10);
    });

    $("#top15unittestbutton").click(function() {
      topxUnitTests(15);
    });

    $("#top25unittestbutton").click(function() {
      topxUnitTests(25);

    // Top languages with unittests and CI
    $("#top10testcibutton").click(function() {
      topxUnitTestsCi(10);
    });

    $("#top15testcibutton").click(function() {
      topxUnitTestsCi(15);
    });

    $("#top25testcibutton").click(function() {
      topxUnitTestsCi(25);
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

function topxCommitedRepos(x) {
    $.getJSON("/_topxcommits", {'topx': x}, function(data) {
        $('#top10committbody').html("");
        $.each(data.top10, function(key,val) {
            $('#top10committbody').append('<tr><td>'+val[0]+'</td><td>'+val[1]+'</td></tr>');
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

function topxLanguages(x) {
    $.getJSON("/_topxunittestci", {'topx': x}, function(data) {
        $('#top10testcitbody').html("");
        $.each(data.top10, function(key,val) {
            $('#top10testcitbody').append('<tr><td>'+val[0]+'</td><td>'+val[1]+'</td></tr>');
        });
    });
}