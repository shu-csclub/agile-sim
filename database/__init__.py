import pandas as pd
from flask import Flask


def init_app(app: Flask):
    global books
    global games
    global shows

    books = pd.read_csv("database/books.csv")
    games = pd.read_csv("database/games.csv")
    shows = pd.read_csv("database/shows.csv")
