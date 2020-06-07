from flask import Blueprint
from mongodb_flask import mongo

main = Blueprint("main", __name__)

@main.route("/")
def index():
    user_collection = mongo.db.users
    # user_collection.insert({"name": "Atreyee"})
    user_collection.insert({"name": "Atreyee Mukherjee"})
    return "<h1>Added a name</h1>"

@main.route('/find')
def find():
    user_collection = mongo.db.users
    user = user_collection.find_one({"name": "Atreyee"})
    return f'<h1>User: {user["name"]} id: {user["_id"]} </h1>'

@main.route('/update')
def update():
    user_collection = mongo.db.users
    user = user_collection.find_one({"name": "Atreyee"})
    user["gender"] = "Female"
    user_collection.save(user)
    return "<h1>Updated</h1>"