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
    def find_by_id(msg_id, self_id):
        """find message record by message id
        format [(Message, nickname)]
        """
        # only the author(self_id) can find his/her hidden/drafted message
        result = db.session.query(Message, User.nickname, User.user_id) \
            .join(User, User.user_id == Message.user_id) \
            .filter(or_(and_(Message.hidden == 0, Message.drafted == 0), User.user_id == self_id),
                    Message.message_id == msg_id) \
            .all()
        return result

    @staticmethod
    def find_by_user(user_id):
        """find messages published by user_id"""
        result = Message.query.filter_by(user_id=user_id).all()
        return result

    @staticmethod
    def find_self_message(self_id, offset, length):
        """query author's(self_id) own messages, return records from offset to offset + length"""
        result = db.session.query(Message, User.nickname, User.avatar) \
            .join(User, User.user_id == Message.user_id) \
            .filter(Message.user_id == self_id) \
            .order_by(Message.message_id.desc()).limit(length).offset(offset).all()
        return result

    @staticmethod
    def get_statistics(self_id):
        """return basic statistics of author's(self_id) messages"""
        total = Message.query.filter_by(user_id=self_id).all()
        result = [0, 0, 0, 0]
        for m in total:
            result[0] += 1
            if m.hidden:
                result[1] += 1
            if m.drafted:
                result[2] += 1
        return result

    @staticmethod
    def count_user_message(user_id):
        return Message.query.filter_by(user_id=user_id).count()

    @staticmethod
    def insert_message(user_id, msg_type, headline, content, drafted=False):
        """add a new message"""
        msg = Message(user_id=user_id, type=msg_type, headline=headline,
                      content=content, drafted=drafted)
        db.session.add(msg)
        db.session.commit()

        return msg.message_id

    @staticmethod
    def update_message(msg_id, msg_type, headline, content, drafted=False):
        """update message of msg_id"""
        msg = db.session.query(Message).filter_by(message_id=msg_id).first()
        print(msg.message_id)
        if msg is None:
            return 0
        msg.type = msg_type
        msg.headline = headline
        msg.content = content
        msg.drafted = drafted
        db.session.commit()
        return msg.message_id

    @staticmethod
    def hide_message(msg_id, self_id):
        # prevent user from altering other's message
        result = Message.query \
            .filter(Message.message_id == msg_id, Message.user_id == self_id).all()
        if len(result) == 1:
            result[0].hidden = 1
            db.session.commit()

    @staticmethod
    def show_message(msg_id, self_id):
        # prevent user from altering other's message
        result = Message.query \
            .filter(Message.message_id == msg_id, Message.user_id == self_id).all()
        print('show', result)
        if len(result) == 1:
            result[0].hidden = 0
            db.session.commit()

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
            .join(User, User.user_id == Message.user_id) \
            .filter(Message.type == msg_type, Message.hidden == 0, Message.drafted == 0) \
            .order_by(Message.message_id.desc()).limit(length).offset(offset).all()
        return result

    @staticmethod
    def count_msg_of_type(msg_type):
        """return number of messages of certain type"""
        result = Message.query \
            .filter(Message.type == msg_type, Message.hidden == 0, Message.drafted == 0) \
            .count()
        return result

    @staticmethod
    def find_top(msg_type, length):
        """return the first length messages of msg_type sorted by reply_count"""
        result = db.session.query(Message, User.nickname, User.avatar) \
            .join(User, User.user_id == Message.user_id) \
            .filter(Message.type == msg_type, Message.hidden == 0, Message.drafted == 0) \
            .order_by(Message.reply_count.desc()).limit(length).all()
        return result

    @staticmethod
    def fuzzy_search(f_keyword, offset, length):
        """fuzzy search messages' content and headline, return records from offset to offset + length"""
        result = db.session.query(Message, User) \
            .join(User, User.user_id == Message.user_id) \
            .filter(or_(Message.headline.like(f_keyword), Message.content.like(f_keyword)),
                    Message.hidden == 0, Message.drafted == 0) \
            .order_by(Message.reply_count.desc()).limit(length).offset(offset).all()
        return result

    @staticmethod
    def count_fuzzy_result(f_keyword):
        """return the number of records that satisfy the fuzzy search condition"""
        result = db.session.query(Message) \
            .filter(or_(Message.headline.like(f_keyword), Message.content.like(f_keyword)),
                    Message.hidden == 0, Message.drafted == 0).count()
        print(result)
        return result
