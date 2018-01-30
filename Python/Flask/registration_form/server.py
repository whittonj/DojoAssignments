from flask import Flask, render_template, request, redirect, flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)    
app.secret_key = 'ThisIsSecret'

@app.route('/')          
def root():
  return render_template('index.html')   

@app.route('/results', methods=['POST'])
def results():
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
  if len(request.form['pw']) < 8:
    flash("Password is too short!")
    failed = True 
  if request.form['pw'] != request.form['pw_confirm']:
    flash("Passwords do not match!")
    failed = True
  
  if failed == True:
    return render_template('failed.html', name = request.form['first_name']) 
  else:
    return render_template('output.html', name = request.form['first_name'])

app.run(debug=True)      