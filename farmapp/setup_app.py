import os

from flask import Flask
from flask_restplus import Api
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = None
db = None
api = None
mail = None

def _seutp_app_singleton(app, db, api, mail):
    if not app or not db or not api or not mail:
        app = Flask('FarmDB',
                    static_folder=os.path.join(os.path.dirname(__file__), "..", "static"),
                    template_folder="templates", )
        CORS(app)
        mail = Mail(app)
        db = SQLAlchemy(app)
        db.init_app(app)
        db.create_all()

        api = Api(app)

        app.config.from_object("farmapp.config")
        db.init_app(app)

        return app, db, api, mail

app, db, api, mail = _seutp_app_singleton(app, db, api, mail)

def get_db_session():
    return db

#db = LocalProxy(db)