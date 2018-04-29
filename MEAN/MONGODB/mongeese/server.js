const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');

const port = process.env.PORT || 8000;
const app = express();
const mongoose = require('mongoose');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'static')));
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

mongoose.connect('mongodb://localhost/mongeese');

const animalSchema = new mongoose.Schema({
    name: String,
    legs: Number,
    type: String
  });
  
const Animal = mongoose.model('Animal', animalSchema);

// Routes
app.get('/', function(req, res){
    Animal.find({}, function(err, results){
      if (err) { console.log(err); }
      res.render('index', { animals: results });
    });
  });
  
  // Create
  app.post('/', function(req, res){
    // Create new animal
    Animal.create(req.body, function(err, result){
      if (err) { console.log(err); }
      res.redirect('/')
    });
  });
  
  // New
  app.get('/new', function(req, res){
    res.render('new');
  });
  
  // Show
  app.get('/:id', function(req, res){
    Animal.find({ _id: req.params.id }, function(err, response) {
      if (err) { console.log(err); }
      res.render('show', { animal: response[0] });
    });
  });
  
  app.get('/:id/edit/', function(req, res){
    Animal.find({ _id: req.params.id }, function(err, response) {
      if (err) { console.log(err); }
      res.render('edit', { animal: response[0] });
    })
  });
  
  // Update
  app.post('/:id', function(req, res){
    Animal.update({ _id: req.params.id }, req.body, function(err, result){
      if (err) { console.log(err); }
      res.redirect('/');
    });
  });
  
  // Delete
  app.post('/:id/delete', function(req, res){
    Animal.remove({ _id: req.params.id }, function(err, result){
      if (err) { console.log(err); }
      res.redirect('/');
    });
  });

  const server = app.listen(port, () => console.log(`Listening on port ${ port }`));
