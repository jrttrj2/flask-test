import os
import sys
from flask import Flask

app = Flask("Flask Test")

@app.route("/")
def index():
    return "Hello World, it is I!"
