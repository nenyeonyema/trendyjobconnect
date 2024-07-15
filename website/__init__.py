#!/usr/bin/python3
""" Init file for all import and app initialiazation
"""
from flask import Flask
import os
from dotenv import load_dotenv


def create_app():
    """ Loads env var and initializes the app
    """
    load_dotenv()

    app = Flask(__name__)


    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    from .views.views import views
    from .views.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    return app
