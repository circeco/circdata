import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'circdata'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://Circeco:Planet20@cluster0-bsyeh.mongodb.net/circdata?retryWrites=true&w=majority')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_circular_initiative')
def get_circular_initiative():
    return render_template("tasks.html", circular_initiative=mongo.db.circular_initiative.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT','8000')),
            debug=True)