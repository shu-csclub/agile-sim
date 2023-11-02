from flask import Blueprint
import services

shows = Blueprint("shows", __name__)


@shows.route("/")
def getAllShows():
    return services.showService.getAll()
