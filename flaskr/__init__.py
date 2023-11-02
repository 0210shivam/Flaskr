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


# accessing something with url parameters - /login?key=value - used with GET methods.
@app.route('/login', methods=['GET'])
def login():
    word = request.args.get('key', 'default')
    return {"message": word}


# In the request body, select the "form-data" option.
@app.route('/signup', methods=['POST'])
def signup():
    key = request.form.get('name', 'default')  # no need to provide default, automatic provides None
    key2 = request.form['age']  # this will cause an error if default not provide.
    return {"data": [key, key2]}


@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']

    if uploaded_file:
        # Process the file here if needed
        file_content = uploaded_file.read()

        # You can process the file content as needed and return it
        return file_content

    return "No file uploaded", 400  # Returning a valid response.
