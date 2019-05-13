import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# If statement to ensure env vars and debug are set appropriately for deployment

if os.environ.get('C9_HOSTNAME'):
    import config
    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = config.MONGO_URI
    app.config['DB_NAME'] = config.DB_NAME
else:
    app.config['DEBUG'] = False
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    app.config["DB_NAME"] = os.getenv("DB_NAME")
    
# Init Mongo app through Flask_PyMongo

mongo = PyMongo(app)

# Read 

@app.route('/')
@app.route('/browse_spells')
def browse_spells():
    return render_template("view_spells.html", spells=mongo.db.spells.find())
     
# Create 

@app.route('/add_spell')
def add_spell():
    return render_template("add_spell.html", components=mongo.db.components.find(), 
    spells=mongo.db.spells.find(), die=mongo.db.die.find(),
    level=mongo.db.level.find(), school=mongo.db.school.find())
    
@app.route('/insert_spell', methods=['POST'])
def insert_spell():
    spells = mongo.db.spells
    spells.insert_one(request.form.to_dict())
    return redirect(url_for('browse_spells'))
    
# Delete

@app.route('/delete_spell/<spell_id>')
def delete_spell(spell_id):
    mongo.db.spells.remove({'_id': ObjectId(spell_id)})
    return redirect(url_for('browse_spells'))    
    
# Update

#10/05/19 edit spell will retrive the correct object from mongodb


@app.route('/edit_spell/<spell_id>')
def edit_spell(spell_id):
    the_spell = mongo.db.spells.find_one({"_id": ObjectId(spell_id)})
    return render_template('edit_spell.html', spell=the_spell, 
    components=mongo.db.components.find(), die=mongo.db.die.find(), level=mongo.db.level.find(),
    school=mongo.db.school.find())
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')))
        