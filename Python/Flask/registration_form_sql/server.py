from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'emails')

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)    
app.secret_key = 'ThisIsSecret'

@app.route('/')          
def index():
  return render_template('index.html')   

@app.route('/results', methods=['POST'])
def results():
  failed = False
  if len(request.form['email']) < 1:
    flash("email cannot be empty!")
    failed = True 
  if not EMAIL_REGEX.match(request.form['email']):
    flash("email not valid")
    failed = True
  if failed == True:
    return render_template('failed.html', name = request.form['email']) 
  else:
    query = "INSERT INTO emails (email, created_at) VALUES (:email, NOW())"
    data = {
      'email': request.form['email'],
    }
    mysql.query_db(query, data)
    emails = mysql.query_db("SELECT * FROM emails")
    print emails
    return render_template('results.html', all_emails = emails)

app.run(debug=True)      