from flask import Flask
import database
import services

app = Flask(__name__)

database.init()
services.init()

version = 'v0.0.0'

@app.route("/books")
def getAllBooks():
    return services.bookService.getAll()

@app.route("/books/popular")
def getPopularBooks():
    return services.bookService.getPopularBooks()

@app.route("/games")
def getAllGames():
    return services.gameService.getAll()

@app.route("/shows")
def getAllShows():
    return services.showService.getAll()