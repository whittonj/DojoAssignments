//copied from solution - much shorter code than I wrote//
const session = require('express-session');
const bodyParser = require('body-parser');
const express = require('express');
const path = require('path');
const port = process.env.PORT || 8000;
const app = express();
//config session-- I did this wrong first go, did not do this much config//
const sessionConfig  = {
  saveUninitialized: true,
  resave: false,
  name: 'session',
  secret: '12345678'
};
//set views//
app.set('view engine', 'ejs');
app.set('views', path.resolve('views'));
//body parser//
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.resolve('assets')));
app.use(session(sessionConfig));

app.get('/', (request, response) => {
  response.render('index', { counter: addOneToCounter(request) });
});

app.post('/by-two', (request, response) => {
  addOneToCounter(request);

  response.redirect('/');
});

app.post('/reset', (request, response) => {
  request.session.destroy();

  response.redirect('/');
});

function addOneToCounter(request) {
  return request.session.counter = request.session.counter ?
                                    request.session.counter + 1 : 1;
}

app.listen(port, () => console.log(`listening on port ${ port }`));
