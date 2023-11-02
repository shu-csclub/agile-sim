from api.v1.books import books
from api.v1.games import games
from api.v1.shows import shows
from api.v1.v1 import v1
from flask import Flask

def init(app: Flask):
    v1.register_blueprint(books, url_prefix="/books")
    v1.register_blueprint(games, url_prefix="/games")
    v1.register_blueprint(shows, url_prefix="/shows")
    app.register_blueprint(v1, url_prefix="/api/v1")