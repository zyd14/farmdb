"""

Project: farmdb

File Name: farmapp.py

Author: Zachary Romer, zach@scharp.org

Creation Date: 8/24/19

Version: 1.0

Purpose:

Special Notes:

"""
import os
from typing import List


from flask import Flask, Blueprint

from farmapp.api import views as api_views
from farmapp.frontend import views as front_views

from farmapp.setup_app import api, app, db

blueprints = [front_views.frontend, api_views.plants]


def blueprints_fabric(app: Flask, blueprint: List[Blueprint]):
    for b in blueprint:

        app.register_blueprint(b)

def configure_logging(app):
    """Configure file(info) and email(error) logging."""

    import logging

    # Set info level on logger, which might be overwritten by handers.
    # Suppress DEBUG messages.
    app.logger.setLevel(logging.INFO)

    # info_log = os.path.join(app.config["LOG_FOLDER"], "info.log")
    # info_file_handler = logging.l.RotatingFileHandler(
    #     info_log, maxBytes=100000, backupCount=10
    # )
    # info_file_handler.setLevel(logging.INFO)
    # info_file_handler.setFormatter(
    #     logging.Formatter(
    #         "%(asctime)s %(levelname)s: %(message)s " "[in %(pathname)s:%(lineno)d]"
    #     )
    # )
    # app.logger.addHandler(info_file_handler)
    #
    # # Testing
    # # farmapp.logger.info("testing info.")
    # # farmapp.logger.warn("testing warn.")
    # # farmapp.logger.error("testing error.")
    #
    # mail_handler = logging.handlers.SMTPHandler(
    #     app.config["MAIL_SERVER"],
    #     app.config["MAIL_USERNAME"],
    #     app.config["ADMINS"],
    #     "O_ops... %s failed!" % app.config["PROJECT"],
    #     (app.config["MAIL_USERNAME"], app.config["MAIL_PASSWORD"]),
    # )
    # mail_handler.setLevel(logging.ERROR)
    # mail_handler.setFormatter(
    #     logging.Formatter(
    #         "%(asctime)s %(levelname)s: %(message)s " "[in %(pathname)s:%(lineno)d]"
    #     )
    # )
    # app.logger.addHandler(mail_handler)

#app, api = create_app()


if __name__ == '__main__':

    blueprints_fabric(app, blueprints)

    configure_logging(app)
    db.create_all()

    api.app.run(debug=True)