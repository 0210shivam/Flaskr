from flask import Flask

app = Flask(__name__)


# first test for index route
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
