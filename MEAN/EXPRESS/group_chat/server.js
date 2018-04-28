const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const port = process.env.PORT || 8000;
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'static')));
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

const server = app.listen(port, () => console.log(`Listening on port ${ port }`));



// load the routes file, pass app and server into it (for handling url visits and events)
require('./routes/index.js')(app, server);
