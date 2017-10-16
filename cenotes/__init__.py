import os
import sys
from flask import Flask
from flask_migrate import Migrate
import nacl.secret
from cenotes.models import db
from cenotes import controllers, errors
from cenotes.utils.crypto import craft_key_from_password

migrate = Migrate()

if sys.version_info[0] < 3:
    raise RuntimeError("Must be using Python 3!")


def create_app(app_settings=None):
    app = Flask(__name__)
    app.config.from_object(app_settings or os.environ['APP_SETTINGS'])
    db.init_app(app)
    migrate.init_app(app, db)

    app.server_box = nacl.secret.SecretBox(
        craft_key_from_password(app.config["SERVER_ENCRYPTION_KEY"]))

    app.register_blueprint(controllers.notes_bp)
    app.register_blueprint(errors.error_bp)
    return app
