from flask import Blueprint
import services

books = Blueprint("book", __name__)


@books.route("/")
def getAllBooks():
    return services.bookService.getAll()


@books.route("/popular")
def getPopularBooks():
    return services.bookService.getPopularBooks()
