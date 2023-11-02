from app.services.BookService import BookService
from app.services.GameService import GameService
from app.services.ShowService import ShowService
from flask import Flask


def init_app(app: Flask):
    global bookService
    global gameService
    global showService

    bookService = BookService()
    gameService = GameService()
    showService = ShowService()
