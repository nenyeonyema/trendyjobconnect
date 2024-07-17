import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MYSQL_URL = os.getenv("MYSQL_URI")
    MYSQL_DBNAME = os.getenv("MYSQL_DBNAME")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = os.getenv("MYSQL_PORT")
