from flask import Blueprint, current_app

v1 = Blueprint("api", __name__)


@v1.route("/")
def index():
    return {"name": "Agile Sim", "version": current_app.config["APPLICATION_VERSION"]}
