$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];

    var language_count = {}

    //receive details from server
    socket.on('language_count', function(msg) {
        console.log("Received lang count: " + msg.language + " - " + msg.count);
        language_count[msg.language] = msg.count;

        $('#log').html(JSON.stringify(language_count));
    });
    socket.on('lang_count_list', function(msg) {
	console.log("Received lang count: " + msg.msg);
	
	$('#log').html(JSON.stringify(msg.msg));
	
    });
});
