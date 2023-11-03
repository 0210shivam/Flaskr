from flask import Flask
from .sample import sample  # we used (.) to show relative path

app = Flask(__name__)

app.register_blueprint(sample.sample_bp)


# To test database connection -
@app.route('/add')
def add_data():
    from .config.db_config import initialize_mongo
    mongo = initialize_mongo()  # we will use this to blueprints. we can use factory method too.

    mongo.db.todos.insert_one({'title': "todo title", 'body': "todo body"})
    return "success done"
