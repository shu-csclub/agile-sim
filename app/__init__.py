import json
import database
from flask import Flask
from app import api, services

def create_app():
    app = Flask(__name__)
    app.config.from_file("config.json", load=json.load)

    database.init_app(app)
    services.init_app(app)
    api.init_app(app)

    return app