from services.BookService import BookService
from services.GameService import GameService
from services.ShowService import ShowService
from flask import Flask


def init_app(app: Flask):
    global bookService
    global gameService
    global showService

    bookService = BookService()
    gameService = GameService()
    showService = ShowService()
