import os
import pytest

from web_dynamic.app import return_app
# print(app)

@pytest.fixture()
def app():
    app = return_app()
    with app.app_context():
        pass

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
