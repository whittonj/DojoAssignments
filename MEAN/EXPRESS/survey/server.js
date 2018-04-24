//copied from solution - much shorter code than I wrote//
const bodyParser = require('body-parser');
const express = require('express');
const path = require('path');
const port = process.env.PORT || 8000;
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

//Moved from solution instead of writing it here in case this is best practice. we're going to have /routes/index.js handle all of our routing
require('./routes/index.js')(app);

app.listen(port, () => console.log(`listening on port ${ port }`));
