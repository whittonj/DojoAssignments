module.exports = function Route(app){
	// root route to render the index.ejs view. changed from my original to see how this works.
	app.get('/', function(req, res) {
	 res.render("index");
	});

	app.post('/results', function(req, res) {
		const submittedInfo = {
			name: req.body.name,
			dojoLocation: req.body.dojoLocation,
			favoriteLanguage: req.body.favoriteLanguage,
			comment: req.body.comment
    };

	 	res.render("results", { userData: submittedInfo });
	});
};