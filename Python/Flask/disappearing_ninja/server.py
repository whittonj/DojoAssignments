from flask import Flask, render_template, request, redirect  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
def root():
  return render_template('index.html')   # Return the string 'Hello World!' as a response.

@app.route('/ninja')
def ninjas():
  return render_template('ninja.html')

@app.route('/ninja/<color>')
def colors(color):
  print color
  return render_template('non.html')

@app.route('/ninja/red')
def red():
  return render_template('red.html')

@app.route('/ninja/blue')
def blue():
  return render_template('blue.html')

@app.route('/ninja/orange')
def orange():
  return render_template('orange.html')

@app.route('/ninja/purple')
def purple():
  return render_template('purple.html')

app.run(debug=True)      # Run the app in debug mode.