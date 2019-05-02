import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'dnd_project3'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tuser@myfirstcluster-rxis3.mongodb.net/dnd_project3?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')
@app.route('/browse_spells')
def browse_spells():
    return render_template("view_spells.html", spells=mongo.db.spells.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        