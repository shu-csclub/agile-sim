from flask import Blueprint
from app import services

books = Blueprint("book", __name__)


@books.route("/")
def getAllBooks():
    return services.bookService.getAll()


@books.route("/recommended")
def getRecommendedBooks():
    return services.bookService.getRecommended()

@books.route("/publishers")
def getUniquePublishers():
    return {
        "publishers": services.bookService.getUniquePublishers()
    }