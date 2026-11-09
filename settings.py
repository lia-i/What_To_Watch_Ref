import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'


