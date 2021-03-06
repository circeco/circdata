import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

DBS_NAME = "circdata"

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'circdata'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


# Homepage
@app.route("/")
def home():
    return render_template("index.html", 
                            initiative_name=mongo.db.initiative_name.find().sort("circular_initiative", 1),
                            initiatie_type=mongo.db.initiatie_type.find().sort("circular_initiative", 1),
                            initiatie_object=mongo.db.initiatie_object.find().sort("circular_initiative", 1),
                            initiatie_description=mongo.db.initiatie_description.find().sort("circular_initiative", 1),)


# Searching box
@app.route('/search/', methods=['GET', 'POST'])
def search(): 
    keyword = request.form.get('search')
    query = ( { "$text": { "$search": keyword } } )
    results = mongo.db.circular_initiative.find(query)
    return render_template("view.html", circular_initiative=results, count=results.count())


# Sort by object 
@app.route('/sort/<keyword>')
def sort(keyword): 
    query = ( { "$text": { "$search": keyword } } )
    results = mongo.db.circular_initiative.find(query)
    return render_template("view.html", circular_initiative=results, count=results.count())


# Display results of the search
@app.route("/results/<result>")
def results(result):
    return render_template("view.html", circular_initiative=result)


# View circular initiatives
@app.route('/get_circular_initiative')
def get_circular_initiative():
    results = mongo.db.circular_initiative.find()
    return render_template("view.html", circular_initiative=results)
        

# Find initiative by object
@app.route("/initiative_by_object", methods=["GET"])
def initiative_by_object():
    a = mongo.db.circular_initiative.find({"initiative_object": {"$regex": '/A/i'}})
    mongo.db.goods_services.find()
    return render_template("view.html",
                            circular_initiative=mongo.db.circular_initiative.find().sort([
                                ("initiative_object", 1)]))


# Add initiative form 
@app.route('/add_initiative')
def add_initiative():
    return render_template('add.html', 
                            circular_initiative=mongo.db.circular_initiative.find(),
                            categories=mongo.db.categories.find(), 
                            goods_services=mongo.db.goods_services.find())


# Post a new initiative
@app.route('/insert_initiative', methods=['POST'])
def insert_initiative():
    submit = {
        "initiative_name" : request.form.get("initiative_name"),
        "initiative_description" : request.form.get("initiative_description"),
        "initiative_type" : request.form.get("initiative_type"),
        "initiative_object" : request.form.getlist("initiative_object"),
        "weblink" : request.form.get("weblink")
    }
    circular_initiative = mongo.db.circular_initiative
    circular_initiative.insert_one(submit)

    return redirect(url_for('get_circular_initiative'))


# Editing an initiative
@app.route("/edit_initiative/<initiative_id>")
def edit_initiative(initiative_id):
    the_initiative = mongo.db.circular_initiative.find_one({"_id": ObjectId(initiative_id)})
    all_initiative_types = mongo.db.categories.find()
    all_goods_services = mongo.db.goods_services.find()
    return render_template("edit.html", circular_initiative=the_initiative, 
                            categories=all_initiative_types, goods_services=all_goods_services)


# Updating initiative data
@app.route('/update_initiative/<initiative_id>', methods=["POST"])
def update_initiative(initiative_id):
    circular_initiative = mongo.db.circular_initiative
    circular_initiative.update({'_id': ObjectId(initiative_id)},
    {
        'initiative_name': request.form.get('initiative_name'),
        'initiative_type': request.form.get('initiative_type'),
        'initiative_description': request.form.get('initiative_description'),
        'initiative_object': request.form.getlist('initiative_object'),
        'weblink': request.form.get('weblink'),
    })
    return redirect(url_for('get_circular_initiative'))


# Delete initiative from database
@app.route("/delete_initiative/<circular_initiative_id>")
def delete_initiative(circular_initiative_id):
    mongo.db.circular_initiative.remove({"_id": ObjectId(circular_initiative_id)})
    return redirect(url_for("get_circular_initiative"))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT','8000')),
            debug=True)