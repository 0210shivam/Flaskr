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
    return {"message": "Hello World"}  # returning a json response.

# Resolving error - use Jsonify or python dictionary to json response.


# Having Two methods - to check method use request object
@app.route('/methods', methods=['GET', 'POST'])  # Debug done to this line
def methods():
    if request.method == 'POST':
        return {"message": "Hello world, this is POST method"}  # returning a json response.
    else:
        return {"message": "Hello World, this is GET method"}  # returning a json response.

# You can also separate both request into different function.
# If GET is present, Flask automatically adds support for the HEAD method and handles HEAD requests according to the HTTP RFC. Likewise, OPTIONS is automatically implemented for you.


# you can also return template if there is any
@app.route('/tempfile')
def showfile():
    return render_template('index.html')
