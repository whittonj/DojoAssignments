from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'thewall')

import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = 'ThisIsSecret'

@app.route('/')          
def index():
  if session.get('email') != None:
    messages = mysql.query_db("SELECT * FROM messages JOIN users ON messages.user_id=users.id;") 
    return render_template('wall.html', all_messages = messages)
  else: 
    messages = mysql.query_db("SELECT * FROM messages JOIN users ON messages.user_id=users.id;")
    return render_template('index.html', all_messages = messages)   

@app.route('/results', methods=['POST'])
def results():
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
    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    password =(request.form['password'])
    pw = md5.new(password).hexdigest()
    email=request.form['email']
    query = "INSERT INTO users (email, first_name, last_name, password, created_at) VALUES (:emailf,:first_name, :last_name, :password,  NOW())"
    data = {
      'emailf': request.form['email'],
      'first_name': request.form['first_name'],
      'last_name':  request.form['last_name'],
      'password': pw
    }
    mysql.query_db(query, data)
    queryb = "SELECT * FROM users WHERE email=:email"   
    data = {
      "email":email
    }               
    user = mysql.query_db(queryb,data)     
    session['user_id'] = user[0]['id']
    return redirect('/')

@app.route('/message', methods=['POST'])
def message():
    query = "INSERT INTO messages (messagetext, created_at, user_id) VALUES (:messagetext, NOW(), :usid)"
    data = {
      'messagetext': request.form['message'],
      'usid': session['user_id']
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/comment', methods=['POST'])
def comment():
    query = "INSERT INTO comments (comment_text, created_at, user_id, message_id) VALUES (:commenttext, NOW(), :usid, 1)"
    data = {
      'commenttext': request.form['comment'],
      'usid': session['user_id'],
      'mess_id': messages['id']
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)      

