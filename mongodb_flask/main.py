from flask import Blueprint
from mongodb_flask import mongo

main = Blueprint("main", __name__)

@main.route("/")
def index():
    user_collection = mongo.db.users
    # user_collection.insert({"name": "Atreyee"})
    user_collection.insert_one({"name": "Atreyee"})
    return "<h1>Added a name</h1>"