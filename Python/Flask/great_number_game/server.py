from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)  
app.secret_key = 'ThisIsSecret'

                         
@app.route('/')      
def root():
    return render_template('index.html')  

@app.route('/reset')
def reset():
    session['secret'] = random.randrange(1, 100)
    session['message'] = "Make a guess >"
    return redirect('/') 

@app.route('/process', methods=['POST'])
def process():
    session['guess']  = int(request.form['guess'])
    if session['guess'] == session['secret']:
        return redirect('/win')
    elif session['guess'] > session['secret']:
        session['message'] = "You guessed", session['guess'],". Your guess is too HIGH"
        return redirect('/')
    elif session['guess'] < session['secret']:
        session['message'] = "You guessed", session['guess'],". Your guess is too LOW"
        return redirect('/')

@app.route('/win')
def win():
    session['message'] = "YOU WIN ! Click button to restart"
    return redirect('/') 

@app.route('/lose')
def lose():
    return render_template('lose.html') 

@app.route('/high')
def high():
    return render_template('high.html') 

app.run(debug=True)      # Run the app in debug mode.