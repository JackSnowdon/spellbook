import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Debugger for running locally, change to False when pushing to heroku

app.config['DEBUG'] = True
#app.config["MONGO_DBNAME"] = 'dnd_project3'
#app.config["MONGO_URI"] = 'mongodb+srv://root:r00tuser@myfirstcluster-rxis3.mongodb.net/dnd_project3?retryWrites=true'

# If statement to ensure env vars are set running locally or on heroku

if app.config["DEBUG"] == True:
    import config
    app.config['MONGO_URI'] = config.MONGO_URI
    app.config['DB_NAME'] = config.DB_NAME
else:
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    app.config["DB_NAME"] = os.getenv("DB_NAME")

mongo = PyMongo(app)

@app.route('/')
@app.route('/browse_spells')
def browse_spells():
    return render_template("view_spells.html", spells=mongo.db.spells.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')))
        