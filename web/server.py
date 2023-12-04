from flask import Flask
from main_lib.component import Component

# Creating Flask app and register routes
app = Flask(__name__)


@app.route("/", methods=["GET"])
def pong_handler():
    return "pong"


@app.route("/create", methods=["POST"])
def create_component_handler():
    c = Component.create_component("main_lib/example.yaml")
    return c.pong()
