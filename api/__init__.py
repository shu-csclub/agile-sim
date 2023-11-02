from api import v1
from flask import Flask


def init(app: Flask):
    v1.init(app)
