import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'dnd_project3'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tuser@myfirstcluster-rxis3.mongodb.net/dnd_project3?retryWrites=true'

@app.route('/')
def hello():
    return 'Hello World ... again'
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        