import pytest
from app import create_app
from flask import Flask

@pytest.fixture()
def app():
    app = create_app()

    app.config.update({
        "TESTING": True
    })

    yield app

@pytest.fixture()
def client(app: Flask):
    return app.test_client()

@pytest.fixture()
def runner(app: Flask):
    return app.test_cli_runner()