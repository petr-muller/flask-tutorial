import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "ya-will-nevah-knaw")
