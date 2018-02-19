from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'emails')

import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = 'ThisIsSecret'

@app.route('/')          
def index():
    return render_template('index.html')   

@app.route('/users/new')          
def new():
    return render_template('new.html')   

@app.route('/users/<userid>')          
def view(userid):
  query= mysql.query_db("SELECT * FROM emails WHERE id = :sid")
  data = { 'sid': userid }
  emails= mysql.query_db(query, data)
  return render_template('display.html')

@app.route('/post', methods=['POST'])
def post():
  failed = False
  if len(request.form['first_name']) < 1:
    flash("First name cannot be empty!")
    failed = True
  if not request.form['first_name'].isalpha():
    flash("First names may only contain characters, who are you, Ke$ha?") 
    failed = True
  if not request.form['last_name'].isalpha():
    flash("Last names may only contain characters, who are you, Ke$ha?") 
    failed = True
  if len(request.form['last_name']) < 1:
    flash("Last name cannot be empty!")
    failed = True
  if len(request.form['email']) < 1:
    flash("email cannot be empty!")
    failed = True 
  if not EMAIL_REGEX.match(request.form['email']):
    flash("email not valid")
    failed = True
  if len(request.form['password']) < 8:
    flash("Password is too short!")
    failed = True 
  if request.form['password'] != request.form['pw_confirm']:
    flash("Passwords do not match!")
    failed = True
  if len(request.form['email']) < 1:
    flash("email cannot be empty!")
    failed = True 
  if not EMAIL_REGEX.match(request.form['email']):
    flash("email not valid")
    failed = True
  if failed == True:
    return render_template('failed.html', name = request.form['email']) 
  else:    
    password =(request.form['password'])
    pw = md5.new(password).hexdigest()
    query = "INSERT INTO emails (email, first_name, last_name, password, created_at) VALUES (:email,:first_name, :last_name, :password,  NOW())"
    data = {
      'email': request.form['email'],
      'first_name': request.form['first_name'],
      'last_name':  request.form['last_name'],
      'password': pw
    }
    mysql.query_db(query, data)
    return redirect('/users')

@app.route('/users', methods=['GET'])
def users():
    emails = mysql.query_db("SELECT * FROM emails")
    print emails
    return render_template('users.html', all_emails = emails)

app.run(debug=True)      