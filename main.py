from flask import Flask
import json
import api
import database
import services

app = Flask(__name__)
app.config.from_file("config.json", load=json.load)

api.init(app)

database.init()
services.init()