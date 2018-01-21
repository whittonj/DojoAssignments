from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
def root():
  return render_template('index.html')   # Return the string 'Hello World!' as a response.

@app.route('/ninjas')
def ninjas():
  return render_template('ninjas.html')

@app.route('/dojos/new')
def new():
  return render_template('new.html')

app.run(debug=True)      # Run the app in debug mode.