from flask import Flask
from .sample import sample  # we used (.) to show relative path
app = Flask(__name__)

app.register_blueprint(sample.sample_bp)
