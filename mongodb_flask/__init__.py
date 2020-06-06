from flask import Flask
from flask_pymongo import PyMongo
from mongodb_flask.config import Config

app = Flask(__name__)
app.config.from_object(Config)

## Add the extensions
mongo = PyMongo(app)
print(mongo.db)

# ## Registering bluebrints
from mongodb_flask.main import main
app.register_blueprint(main)
