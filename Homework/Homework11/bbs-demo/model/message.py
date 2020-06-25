from flask import session
from model import User
from sqlalchemy import or_, and_
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
    hidden = db.Column(BIT(1), nullable=False, server_default=db.text("b'0'"))
    drafted = db.Column(BIT(1), nullable=False, server_default=db.text("b'0'"))
    recommended = db.Column(BIT(1), nullable=False, server_default=db.text("b'0'"))

    user = db.relationship('User')

    @staticmethod
    def find_by_id(msg_id):
        """find message record by message id"""
        # format [(Message, nickname)]
        # only the author can find his/her hidden/drafted message
        result = db.session.query(Message, User.nickname).join(User, User.user_id == Message.user_id).filter(or_(and_(
            Message.hidden == 0, Message.drafted == 0), User.user_id == session.get('user_id')),
            Message.message_id == msg_id).all()
        return result

    @staticmethod
    def insert_message(msg_type, headline, content, drafted=False):
        """add a new message"""
        user_id = session.get('user_id')
        msg = Message(user_id=user_id, type=msg_type, headline=headline,
                      content=content, drafted=drafted, )
        db.session.add(msg)
        db.session.commit()

        return msg.message_id

    @staticmethod
    def increase_read_count(msg_id):
        """increase message's read count by 1"""
        msg = db.session.query(Message).filter_by(message_id=msg_id).first()
        if msg is None:
            return -1
        else:
            msg.read_count += 1
            db.session.commit()
            return msg.read_count

    @staticmethod
    def increase_reply_count(msg_id):
        """increase message's reply count by 1"""
        msg = db.session.query(Message).filter_by(message_id=msg_id).first()
        if msg is None:
            return -1
        else:
            msg.reply_count += 1
            db.session.commit()
            return msg.reply_count
