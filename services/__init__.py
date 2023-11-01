from services.BookService import BookService
from services.GameService import GameService
from services.ShowService import ShowService

def init():
    global bookService
    global gameService
    global showService

    bookService = BookService()
    gameService = GameService()
    showService = ShowService()