from app.api.books import books
from app.api.games import games
from app.api.shows import shows
from flask import Flask, Blueprint, current_app


def init_app(app: Flask):
    api = Blueprint("api", __name__)

    @api.route("/")
    def index():
        return {
            "name": "Agile Sim",
            "version": current_app.config["APPLICATION_VERSION"],
        }

    api.register_blueprint(books, url_prefix="/books")
    api.register_blueprint(games, url_prefix="/games")
    api.register_blueprint(shows, url_prefix="/shows")
    app.register_blueprint(api, url_prefix="/api")
