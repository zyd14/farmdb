from flask import Flask
from flask_restplus import Api
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy


def _seutp_app():
    app = Flask('FarmDB',
                static_folder=os.path.join(os.path.dirname(__file__), "..", "static"),
                template_folder="templates", )
    mail = Mail(app)
    db = SQLAlchemy(app)
    api = Api(app)

    app.config.from_object("farmapp.config")
    db.init_app(app)

    return app, db, api


app, db, api = _seutp_app()