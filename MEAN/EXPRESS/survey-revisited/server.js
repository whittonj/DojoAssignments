//copied from solution - much shorter code than I wrote//
const bodyParser = require('body-parser');
const express = require('express');
const path = require('path');
const app = express();
//don't need session for this one
const sessionConfig  = {
  saveUninitialized: true,
  resave: false,
  name: 'session',
  secret: '12345678'
};

app.use(bodyParser.urlencoded());
app.use(express.static(path.join(__dirname, "./static")));

app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

//thave /routes/index.js handle all of our routing

var server = app.listen(8000, function() {
  console.log("listening on port 8000");
 });

var route = require('./routes/index.js')(app, server);



