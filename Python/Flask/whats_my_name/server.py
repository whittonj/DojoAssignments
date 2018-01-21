from flask import Flask, render_template, request, redirect  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
def root():
  return render_template('index.html')   # Return the string 'Hello World!' as a response.

@app.route('/process', methods=['POST'])
def process():
  print "Got Post Info"
  # recall the name attributes we added to our form inputs
  # to access the data that the user input into the fields we use request.form['name_of_input']
  name = request.form['name']
  email = request.form['email']
  return redirect('/')

app.run(debug=True)      # Run the app in debug mode.