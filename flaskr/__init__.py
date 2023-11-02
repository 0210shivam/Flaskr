from flask import (Flask,
                   request,  # importing request object
                   render_template)  # importing render_template object

app = Flask(__name__)


# first test for index route
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# defining HTTP methods
@app.route('/hello', methods=['GET'])
def hello():
    return {"Hello World"}  # returning a json response.


# Having Two methods - to check method use request object
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return {"Hello world, this is POST method"}  # returning a json response.
    else:
        return {"Hello World"}  # returning a json response.

# You can also separate both request into different function.
# If GET is present, Flask automatically adds support for the HEAD method and handles HEAD requests according to the HTTP RFC. Likewise, OPTIONS is automatically implemented for you.


# you can also return template if there is any
@app.route('/tempfile')
def showfile():
    return render_template('index.html')
