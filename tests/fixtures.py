import pytest

from app import create_app

from common.models import MODELS
from common.database import DB


@pytest.fixture
def client():
    app = create_app()
    app.config["testing"] = True
    with app.test_client() as client:
        return client


@pytest.fixture(scope="module", autouse=True)
def fake_database():
    yield DB
    DB.drop_tables(MODELS)
    DB.create_tables(MODELS)


def logged_in(client):
    with client.session_transaction() as session:
        session["user_id"] = 1
        session["language"] = "fr"
