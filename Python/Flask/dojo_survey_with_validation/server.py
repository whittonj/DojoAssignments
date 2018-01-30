from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)    
app.secret_key = 'ThisIsSecret'

@app.route('/')          
def root():
  return render_template('index.html')   # Return the string 'Hello World!' as a response.

@app.route('/results', methods=['POST'])
def results():
  if len(request.form['name']) < 1:
    flash("Name cannot be empty!") 
  if len(request.form['location']) < 1:
    flash("Location cannot be empty!") 
  if len(request.form['message']) < 1:
    flash("Comment cannot be empty!") 
  if len(request.form['message']) > 120:
    flash("Comment is too long!") 
  return render_template('output.html', name = request.form['name'], location = request.form['location'], language = request.form['Language'], message = request.form['message'])

app.run(debug=True)      # Run the app in debug mode.