const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const port = process.env.PORT || 8000;
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'static')));
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

mongoose.connect('mongodb://localhost/quoting_dojo');

const quoteSchema = new mongoose.Schema({
    name: String,
    quote: String,
    date: Date
  });
  
  const Quote = mongoose.model('quotes', quoteSchema);
  
  // Point server to views
  app.set('views', path.join(__dirname, 'views'));
  // We're using ejs as our view engine
  app.set('view engine', 'ejs');
  
  // Here are our routes!
  app.get('/', function(req, res) {
    res.render('index');
  });
  
  app.get('/quotes', function(req, res) {
    // Logic to grab all quotes and pass into the rendered view
    Quote.find({}, function(err, quotes) {
      if (err) { console.log(err); }
      console.log(quotes);
      res.render('quotes', { quotes: quotes });
    });
  });
  
  app.post('/quotes', function(req, res) {
    Quote.create(req.body, function(err) {
      if (err) { console.log(err); }
      res.redirect('/quotes');
    });
  });

  const server = app.listen(port, () => console.log(`Listening on port ${ port }`));
