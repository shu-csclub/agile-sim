import pandas as pd
from flask import Flask


def init_app(app: Flask):
    global books
    global games
    global shows

    books = pd.read_csv("database/books.csv", keep_default_na=False)
    games = pd.read_csv("database/games.csv", keep_default_na=False)
    shows = pd.read_csv("database/shows.csv", dtype={'netflix': bool, 'hulu': bool, 'prime_video': bool, 'disney_plus': bool}, keep_default_na=False)
