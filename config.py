import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "ya-will-nevah-knaw")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(BASEDIR, "app.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
