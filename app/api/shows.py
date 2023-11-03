from flask import Blueprint, abort
from app import services

shows = Blueprint("shows", __name__)


@shows.route("/")
def getAllShows():
    return services.showService.getAll()


@shows.route("/old")
def getOldShows():
    return services.showService.getOld()


@shows.route("/services")
def getAllServices():
    return {"services": services.showService.getServices()}
