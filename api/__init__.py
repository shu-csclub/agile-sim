from api import v1
from flask import Flask


def init_app(app: Flask):
    v1.init_app(app)
