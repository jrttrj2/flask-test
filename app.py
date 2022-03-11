import os
import sys
from flask import Flask

from flask_sqlalchemy import SQLAlchemy


# Configuration
app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import models.py, import here to configure db first
from models import Result

# Main App
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<name>")
def hello_name(name):
    return "Hello {}!".format(name)


if __name__== "__main__":
    app.run()