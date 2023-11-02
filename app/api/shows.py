from flask import Blueprint
from app import services

shows = Blueprint("shows", __name__)


@shows.route("/")
def getAllShows():
    return services.showService.getAll()
