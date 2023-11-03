from flask import (Flask,
                   request,  # importing request object
                   render_template,  # importing render_template object
                   make_response,  # importing make_response to create responses
                   redirect,  # importing redirect to desired url
                   url_for)  # importing url_for to create urls

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


# Setting cookie to response object
@app.route('/set_cookie')
def set_cookie():
    resp = make_response("Cookie set")
    resp.set_cookie('user', 'Shiv')
    return resp


# Getting cookie
@app.route('/get_cookie')
def get_cookie():
    user = request.cookies.get('user')
    return f"Hello, {user}"


# To redirect user to another url use this
@app.route('/original')
def original():
    # Redirect to another route using 'redirect' function
    return redirect(url_for('new_route'))


@app.route('/new')
def new_route():
    return "This is the new route."


# To handle any error use errorhandler decorator - this will get any error with code 404 and will show custom template.
# You can set this type of custom error handler templates for any code like - 500 etc...
@app.errorhandler(404)
def page_not_found():
    return render_template('page_not_found.html'), 404


@app.errorhandler(500)
def internal_server_error():
    # Render a custom error template and return it with a 500 status code
    return render_template('500_error.html'), 500
