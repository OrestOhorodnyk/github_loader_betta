import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1291628bb0b13ce0c676dfde280ba678'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///site.db'
    INIT_DB = os.environ.get('INIT_DB')
