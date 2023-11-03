from flask import Blueprint
from app import services

games = Blueprint("games", __name__)


@games.route("/")
def getAllGames():
    return services.gameService.getAll()
