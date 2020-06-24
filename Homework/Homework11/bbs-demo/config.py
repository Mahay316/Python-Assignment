import os

SECRET_KEY = os.urandom(24)

# SQLAlchemy configuration
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:mahay@localhost/bbs"
SQLALCHEMY_TRACK_MODIFICATIONS = True
