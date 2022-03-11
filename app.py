import os
import sys
from flask import Flask

app = Flask("Flask Test")
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def index():
    secret_key = app.config.get("SECRET_KEY")
    return "Hello World! The secret key is " + secret_key + "."
