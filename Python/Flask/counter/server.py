from flask import Flask, render_template, request, redirect, session, flash 
app = Flask(__name__)    
app.secret_key = 'ThisIsSecret'

                         
@app.route('/')         
def root():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1
    return render_template('index.html')  

@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/') 

@app.route('/two')         
def two():
    session['counter'] = session['counter'] + 1
    counter = session['counter']
    print counter
    return redirect('/') 



app.run(debug=True)      # Run the app in debug mode.