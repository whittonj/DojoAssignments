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
    session['str'] = random.randrange(3, 18)
    session['str_mod'] = int(round(session['str']/5,0))
    session['dex'] = random.randrange(3, 18)
    session['dex_mod'] = int(round(session['dex']/5,0))
    session['con'] = random.randrange(3, 18)
    session['con_mod'] = int(round(session['con']/5,0))
    session['wis'] = random.randrange(3, 18)
    session['wis_mod'] = int(round(session['wis']/5,0))
    session['int'] = random.randrange(3, 18)
    session['int_mod'] = int(round(session['int']/5,0))
    session['cha'] = random.randrange(3, 18)
    session['cha_mod'] = int(round(session['cha']/5,0))
    session['max_hp'] = 10 + session['con_mod']
    session['hp'] = session['max_hp']
    session['base_ac'] = 10 + session['dex_mod']
    session['armor'] = "Padded"
    session['arm_mod'] = 1
    session['weapon'] = "Short sword"
    session['weap_dam'] = 6
    session['shield'] = "Buckler"
    session['shie_mod'] = 1
    session['heal_pots'] = 1
    session['gold'] = 0
    session['ac'] = session['base_ac']+ session['arm_mod'] + session['shie_mod']
    session['lvl'] = 1
    session['xp'] = 0
    session['ab'] = session['lvl'] + session['str_mod']
    session['message'] = "Starting a new game >"
    return redirect('/') 

@app.route('/encount', methods=['POST'])
def encount():
    session['enc'] = random.randrange(1, 4)
    if session['enc']  <100:
        session['encounter'] = "Its a fight"
        session['monster'] = "Kobold"
        session['mon_hp'] = 5
        session['mon_dam'] = 6
        session['mon_ab'] = 4
        session['mon_ac'] = 12
        session['mon_xp'] = 25
        session['mon_man'] = "Kobolds are craven reptilian humanoids that commonly infest dungeons. They make up for their physical ineptitude with a cleverness for trap making." 
    return render_template('fight.html')  

@app.route('/process', methods=['POST'])
def process():
    session['action'] = request.form['action'] 
    if session['action'] == 'attack':
        session['message'] = session['message'] + "You attack the " + session['monster'] + "  ----  "
        session['attack_roll'] = random.randrange(1, 20)
        session['message'] = session['message'] + "You rolled a " + str(session['attack_roll']) + "  ----  "
        session['attack'] = session['attack_roll'] + session['ab']
        if session['attack'] > session['mon_ac']:
            session['message'] = session['message'] + "HIT!" + "  ----  "
            session['mon_hp'] = session['mon_hp'] - (random.randrange(1, session['weap_dam']) + session['str_mod'])
            if session['mon_hp'] <= 0:
                session['loot_type'] = random.randrange(1, 100)
                if session['loot_type'] < 101:
                    session['loot_name'] = "gold"
                    session['loot'] = random.randrange(1, session['mon_xp'])
                    session['gold'] = session['gold'] + session['loot']
                session['message'] = session['message'] + "You killed the " + session['monster'] + " ---- "
                session['message'] = session['message'] + "You found " + session['loot_name'] + " ---- "
                session['xp'] = session['xp'] + session['mon_xp']
                return render_template('/loot.html')
        else:
            session['message'] = session['message'] + "You missed!" + "  ----  "
    if session['action'] == 'heal':
        if session['heal_pots'] > 0:
            session['heal_pots'] = session['heal_pots'] -1
            session['heal'] = random.randrange(1,8) * session['lvl']
            session['hp'] = session['hp'] + session['heal']
            if session['hp'] > session['max_hp']:
                session['hp'] = session['max_hp']
            session['message'] = session['message'] + str(session['heal']) + " hps  ----  "
        else:
            session['message'] = session['message'] + "You're out of potions!!! ----"
    #monster turn
    session['message'] = session['message'] + "The " + session['monster'] + " attacks you! ----  "
    session['mon_attack_roll'] = random.randrange(1, 20)
    session['monster_attack'] = session['mon_attack_roll'] + session['mon_ab']
    if session['monster_attack'] > session['ac']:
        session['message'] = session['message'] + "The " + session['monster'] + " HITS YOU! ----  "
        session['hp'] = session['hp'] -  random.randrange(1, session['mon_dam'])
        if session['hp'] < 1:
            return render_template('/dead.html')
    else:
        session['message'] = session['message'] + "The " + session['monster'] + " misses you! ----  "

    return render_template('/fight.html')

app.run(debug=True)      # Run the app in debug mode.