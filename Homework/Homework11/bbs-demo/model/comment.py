from sqlalchemy.dialects.mysql import BIT

from .database import Base, db


class Comment(Base):
    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.user_id'), index=True)
    message_id = db.Column(db.ForeignKey('message.message_id'), index=True)
    content = db.Column(db.Text)
    reply_to = db.Column(db.Integer, nullable=False)
    hidden = db.Column(BIT(1), nullable=False)

    message = db.relationship('Message')
    user = db.relationship('User')
