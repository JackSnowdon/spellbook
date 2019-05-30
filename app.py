import os
from flask import Flask, render_template, redirect, session, request, url_for, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

# If statement to ensure env vars and debug are set appropriately for deployment

if os.environ.get('C9_HOSTNAME'):
    import config
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['MONGO_URI'] = config.MONGO_URI
    app.config['DB_NAME'] = config.DB_NAME
else:
    app.config['DEBUG'] = False
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    app.config["DB_NAME"] = os.getenv("DB_NAME")
    
# Init Mongo app through Flask_PyMongo

mongo = PyMongo(app)

# Read 

@app.route('/')     
@app.route('/index')
def index ():
    return render_template("index.html")

@app.route('/browse_spells')
def browse_spells():
    spell=mongo.db.spells
    results=list(spell.find().sort("spell_name", 1))
    return render_template("view_spells.html", spells=results,
    components=mongo.db.components.find())

# Create spells

@app.route('/add_spell')
def add_spell():
    return render_template("add_spell.html", components=mongo.db.components.find(), 
    spells=mongo.db.spells.find(), die=mongo.db.die.find(),
    level=mongo.db.level.find(), school=mongo.db.school.find())
    
@app.route('/insert_spell', methods=['POST'])
def insert_spell():
    spells = mongo.db.spells
    spells.insert_one({'spell_name':request.form.get('spell_name'),
        'spell_level':request.form.get('spell_level'),
        'school': request.form.get('school'),
        'casting_time': request.form.get('casting_time'),
        'range':request.form.get('range'),
        'components':request.form.getlist('components'),
        'duration':request.form.get('duration'),
        'die_value':request.form.get('die_value'),
        'die_amount':request.form.get('die_amount')})
    return redirect(url_for('browse_spells'))
    
# Delete

@app.route('/delete_spell/<spell_id>')
def delete_spell(spell_id):
    error = None
    if 'username' in session:
        mongo.db.spells.remove({'_id': ObjectId(spell_id)})
        return redirect(url_for('browse_spells'))
    
    else:
        error = "You must be logged in to delete spells"
        return render_template('login.html', error = error)
    
# Update

@app.route('/edit_spell/<spell_id>')
def edit_spell(spell_id):
    the_spell = mongo.db.spells.find_one({"_id": ObjectId(spell_id)})
    component = the_spell['components']
    return render_template('edit_spell.html', spell=the_spell, 
    components=mongo.db.components.find(), die=mongo.db.die.find(), level=mongo.db.level.find(),
    school=mongo.db.school.find(), component=component)

@app.route('/update_spell/<spell_id>', methods=["POST"])
def update_spell(spell_id):
    spells = mongo.db.spells
    spells.update( {'_id': ObjectId(spell_id)},
    {
        'spell_name':request.form.get('spell_name'),
        'spell_level':request.form.get('spell_level'),
        'school': request.form.get('school'),
        'casting_time': request.form.get('casting_time'),
        'range':request.form.get('range'),
        'components':request.form.getlist('components'),
        'duration':request.form.get('duration'),
        'die_value':request.form.get('die_value'),
        'die_amount':request.form.get('die_amount')
    })
    return redirect(url_for('browse_spells'))
    
    
# Search

# 29/05/19 basic accesdeing spell search below. 
    
@app.route('/search_levels')
def search_levels():
    spells=mongo.db.spells
    results=list(spells.find().sort("spell_level", 1))
    return render_template('searched_spells.html', 
            results=results, spells=spells)
    
@app.route('/search_schools', methods=['GET'])
def search_schools():
    spells=mongo.db.spells
    results=list(spells.find().sort("school", 1))
    return render_template('searched_spells.html', 
            results=results, spells=spells)


@app.route('/search_casting', methods=['GET'])
def search_casting():
    spells=mongo.db.spells
    results=list(spells.find().sort("casting_time", 1))
    return render_template('searched_spells.html', 
            results=results, spells=spells)
            
@app.route('/search_duration', methods=['GET'])
def search_duration():
    spells=mongo.db.spells
    results=list(spells.find().sort("duration", 1))
    return render_template('searched_spells.html', 
            results=results, spells=spells)


# Login/Register 

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/register_request', methods=['POST', 'GET'])
def register_request():
    success = None
    error = None
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username':request.form['user_name'].lower()})
        if existing_user is None:
            users.insert({'username':request.form['user_name'].lower()})
            session['username'] = request.form['user_name']
            success = 'You were successfully logged in'
            return render_template('index.html', success = success)
        else:
            error = 'That username has already been taken'
    
    return render_template('register.html', error = error)
    
@app.route('/login')
def login():
    return render_template("login.html")
    
@app.route('/login_request', methods=['POST'])
def login_request():
    success = None
    error = None
    users = mongo.db.users
    login_user = users.find_one({'username':request.form['user_name'].lower()})
    if login_user:
        session['username'] = request.form['user_name']
        success = 'You were successfully logged in'
        return render_template('index.html', success = success)
        
    else:
        error = 'That username does not exist'
    
    return render_template('login.html', error = error)

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   success = None
   session.pop('username', None)
   success = 'You have successfully logged out'
   return render_template('index.html', success = success)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')))
