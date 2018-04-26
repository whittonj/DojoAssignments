module.exports = function Route(app, server){
	// root route to render the index.ejs view. changed from my original to see how this works.
	var io = require('socket.io').listen(server);
	
	app.get('/', function(req, res) {
	 res.render("index");
	});

	io.sockets.on('connection', function (socket) {
		console.log("Client/socket is connected!");
		console.log("Client/socket id is: ", socket.id);

		
		socket.on( "button_clicked", function (data){
			console.log( 'Someone clicked a button!  Reason: '  + data.reason);
			socket.emit( 'server_response', {response:  "sockets are the best!"});
		});

		socket.on("posting_form", function (data) {
		var random_num = Math.floor((Math.random() * 1000) + 1);
		socket.emit('updated_message', {response: data}); 
		socket.emit('random_num', {response: random_num}); 
	   })
		
	  });


};



