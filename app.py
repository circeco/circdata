import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'circdata'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://Circeco:Planet20@cluster0-bsyeh.mongodb.net/circdata?retryWrites=true&w=majority')

mongo = PyMongo(app)


DBS_NAME = "circdata"


# Homepage
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", 
                            initiative_name=mongo.db.initiative_name.find().sort("circular_initiative", 1),
                            initiatie_type=mongo.db.initiatie_type.find().sort("circular_initiative", 1),
                            initiatie_object=mongo.db.initiatie_object.find().sort("circular_initiative", 1),
                            initiatie_description=mongo.db.initiatie_description.find().sort("circular_initiative", 1),)


@app.route('/')
@app.route('/get_circular_initiative')
def get_circular_initiative():
    return render_template("view.html", circular_initiative=mongo.db.circular_initiative.find())


@app.route('/')
@app.route('/add_initiative')
def add_initiative():

    return render_template('add.html', 
                            circular_initiative=mongo.db.circular_initiative.find(),
                            categories=mongo.db.categories.find(), 
                            goods_services=mongo.db.goods_services.find())


@app.route('/insert_initiative', methods=['POST'])
def insert_initiative():
    submit = {
        "initiative_name" : request.form.get("initiative_name"),
        "initiative_description" : request.form.get("initiative_description"),
        "initiative_type" : request.form.get("initiative_type"),
        "initiative_object" : request.form.getlist("initiative_object"),
        "weblink" : request.form.get("weblink")
    }
    circular_initiative =  mongo.db.circular_initiative
    circular_initiative.insert_one(submit)

    return redirect(url_for('get_circular_initiative'))




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT','8000')),
            debug=True)