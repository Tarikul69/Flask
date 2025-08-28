import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret")

    #Super simple SQLite path (database will be in project folder)
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, '../instance/app.db')}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
