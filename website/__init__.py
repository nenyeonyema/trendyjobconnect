from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from .models.user import JobSeeker, Job, Employer, AppliedJob
        db.create_all()

    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_views = 'auth.login'
    login_manager.login_message_category = 'info'

    from .views.home import homepage
    from .views.auth import auth
    from .views.job import job

    app.register_blueprint(homepage)
    app.register_blueprint(auth)
    app.register_blueprint(job)

    return app


@login_manager.user_loader
def load_user(user_id):
    from .models.user import JobSeeker, Employer
    user = JobSeeker.query.get(int(user_id))
    if user is None:
        user = Employer.query.get(int(user_id))
    return user
