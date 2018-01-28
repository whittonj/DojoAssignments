from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)  
app.secret_key = 'ThisIsSecret'

                         
@app.route('/')      
def root():
    return render_template('index.html')  

@app.route('/reset')
def reset():
    session['gold'] = 0
    session['secret'] = random.randrange(1, 100)
    session['message'] = "Starting a new game >"
    return redirect('/') 

@app.route('/process', methods=['POST'])
def process():
    session['building'] = request.form['building'] 
    session['message'] = session['message'] + "You visited the " + session['building'] + "  ----  "
    if session['building'] == 'farm':
        session['gold'] = session['gold'] + random.randrange(10, 20)
    elif session['building'] == 'cave':
        session['gold'] = session['gold'] + random.randrange(5, 10)
    elif session['building'] == 'house':
        session['gold'] = session['gold'] + random.randrange(2, 5)
    elif session['building'] == 'casino':
        session['gold'] = session['gold'] + random.randrange(-50, 50)
    return redirect('/')

@app.route('/win')
def win():
    session['message'] = "YOU WIN ! Click button to restart"
    return redirect('/') 

app.run(debug=True)      # Run the app in debug mode.