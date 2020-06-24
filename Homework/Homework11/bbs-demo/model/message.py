from sqlalchemy.dialects.mysql import BIT

from .database import Base, db


class Message(Base):
    message_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.user_id'), index=True)
    type = db.Column(db.SMALLINT, nullable=False)
    headline = db.Column(db.String(100), nullable=False)
    content = db.Column(db.TEXT)
    read_count = db.Column(db.Integer, nullable=False, server_default=db.text("'0'"))
    reply_count = db.Column(db.Integer, nullable=False, server_default=db.text("'0'"))
    hidden = db.Column(BIT(1), nullable=False)
    drafted = db.Column(BIT(1), nullable=False)
    recommended = db.Column(BIT(1), nullable=False)

    user = db.relationship('User')
