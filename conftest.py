import pytest
from cenotes import create_app, utils, db as _db
from config_backend import Testing


@pytest.fixture(name="app", scope="session")
def _app():
    return create_app(app_settings=Testing)


@pytest.fixture(scope="session")
def db(app):
    _db.drop_all()
    _db.app = app
    _db.create_all()
    yield _db
    _db.drop_all()


@pytest.fixture(scope="session", name="testing_key")
def _key():
    return utils.craft_key_from_password("testing")


@pytest.fixture(scope="session", name="testing_box")
def _box(testing_key):
    return utils.craft_secret_box(testing_key)
