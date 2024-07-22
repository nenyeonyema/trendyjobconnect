from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
# from config import Config
import os
from dotenv import load_dotenv

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config.from_object('config.Config')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

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

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    return app


@login_manager.user_loader
def load_user(user_id):
    from .models.user import JobSeeker, Employer
    user = JobSeeker.query.get(int(user_id))
    if user is None:
        user = Employer.query.get(int(user_id))
    return user
