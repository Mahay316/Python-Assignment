from .database import db
from .user import User
from .message import Message
from .comment import Comment


def init_db(app):
    db.init_app(app)
