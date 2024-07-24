import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADZUNA_APP_ID = os.getenv('ADZUNA_APP_ID')
    ADZUNA_APP_KEY = os.getenv('ADZUNA_APP_KEY')
    RAPIDAPI_HOST = os.getenv('RAPIDAPI_HOST')
    RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')
    JOOBLE_API_KEY = os.getenv('JOOBLE_API_KEY')
    # MYSQL_URL = os.getenv("SQLALCHEMY_DATABASE_URI")
    # MYSQL_DBNAME = os.getenv("MYSQL_DBNAME")
    # MYSQL_USER = os.getenv("MYSQL_USER")
    # MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    # MYSQL_HOST = os.getenv("MYSQL_HOST")
    # MYSQL_PORT = os.getenv("MYSQL_PORT")
