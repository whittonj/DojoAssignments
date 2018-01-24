from flask import Flask, render_template, request, redirect, session  
app = Flask(__name__)    
app.secret_key = 'ThisIsSecret'

                         
@app.route('/')         
def root():
    session['counter'] = session['counter'] + 1
    counter = session['counter']
    print counter
    return render_template('index.html', counter = counter)  

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