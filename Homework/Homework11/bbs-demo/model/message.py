from common import type_map
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
        """find message record by message id
        format [(Message, nickname)]
        """
        # only the author can find his/her hidden/drafted message
        result = db.session.query(Message, User.nickname, User.user_id).join(User,
                                                                             User.user_id == Message.user_id).filter(
            or_(and_(
                Message.hidden == 0, Message.drafted == 0), User.user_id == session.get('user_id')),
            Message.message_id == msg_id).all()
        return result

    @staticmethod
    def find_by_user(user_id):
        """find messages published by user_id"""
        result = Message.query.filter_by(user_id=user_id).all()
        return result

    @staticmethod
    def count_user_message(user_id):
        result = Message.query.filter_by(user_id=user_id).count()
        return result

    @staticmethod
    def insert_message(user_id, msg_type, headline, content, drafted=False):
        """add a new message"""
        msg = Message(user_id=user_id, type=msg_type, headline=headline,
                      content=content, drafted=drafted)
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

    @staticmethod
    def find_limit_of_type(msg_type, offset, length):
        """query messages of msg_type, return records from offset to offset + length"""
        result = db.session.query(Message, User.nickname, User.avatar) \
            .join(User, User.user_id == Message.user_id).filter(Message.type == msg_type) \
            .order_by(Message.message_id.desc()).limit(length).offset(offset).all()
        return result

    @staticmethod
    def count_msg_of_type(msg_type):
        """return number of messages of certain type"""
        result = Message.query.filter(Message.type == msg_type, Message.hidden == 0, Message.drafted == 0).count()
        return result

    @staticmethod
    def find_top(msg_type, length):
        """return the first length messages of msg_type sorted by reply_count"""
        result = db.session.query(Message, User.nickname, User.avatar) \
            .join(User, User.user_id == Message.user_id) \
            .filter(Message.type == msg_type, Message.hidden == 0, Message.drafted == 0) \
            .order_by(Message.reply_count.desc()).limit(length).all()
        return result
