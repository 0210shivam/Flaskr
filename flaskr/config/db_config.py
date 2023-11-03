from flaskr import app
from flask_pymongo import PyMongo
from decouple import config


def initialize_mongo():
    app.config['MONGO_URI'] = config('MONGO_URI')  # Config string using decouple connected to app instance
    mongo = PyMongo(app)  # Running Python mongo driver by passing connection string to it
    return mongo
