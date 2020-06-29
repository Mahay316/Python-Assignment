from model import User
from sqlalchemy.dialects.mysql import BIT

from .database import Base, db


class Comment(Base):
    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.user_id'), index=True)
    message_id = db.Column(db.ForeignKey('message.message_id'), index=True)
    content = db.Column(db.Text)
    reply_to = db.Column(db.Integer, nullable=False)
    reply_to_id = db.Column(db.ForeignKey('user.user_id'), index=True)
    hidden = db.Column(BIT(1), nullable=False, server_default=db.text("b'0'"))

    message = db.relationship('Message')
    user1 = db.relationship('User', foreign_keys=[user_id])
    user2 = db.relationship('User', foreign_keys=[reply_to_id])

    @staticmethod
    def insert_comment(user_id, msg_id, content, reply_to, reply_to_id):
        comment = Comment(user_id=user_id, message_id=msg_id, content=content,
                          reply_to=reply_to, reply_to_id=reply_to_id)
        db.session.add(comment)
        db.session.commit()
        return comment.comment_id

    @staticmethod
    def find_by_id(comment_id):
        """return comment of the certain comment_id"""
        result = Comment.query.filter_by(comment_id=comment_id).all()
        return result

    @staticmethod
    def hide_comment(comment_id):
        """hide the comment of the certain comment_id"""
        result = Comment.query.filter_by(comment_id=comment_id).first()
        if result is not None:
            result.hidden = 1
            db.session.commit()
        return result.comment_id

    @staticmethod
    def find_original_comment(msg_id, offset, length):
        """return all comments of message msg_id
        this static method also prepares for comments pagination
        """
        result = db.session.query(Comment, User).join(User, User.user_id == Comment.user_id) \
            .filter(Comment.message_id == msg_id, Comment.hidden == 0, Comment.reply_to == 0) \
            .order_by(Comment.comment_id.desc()).limit(length).offset(offset).all()
        return result

    @staticmethod
    def count_original_comment(msg_id):
        """return the number of comments of message msg_id"""
        return Comment.query \
            .filter(Comment.message_id == msg_id, Comment.hidden == 0, Comment.reply_to == 0) \
            .count()

    @staticmethod
    def count_user_comment(user_id):
        return Comment.query.filter(Comment.user_id == user_id).count()

    @staticmethod
    def find_reply_by_comment(reply_to):
        """find replies to a certain comment"""
        # reply_to can also constraint the message that the reply belongs to
        result = db.session.query(Comment, User).join(User, User.user_id == Comment.user_id) \
            .filter(Comment.reply_to == reply_to, Comment.hidden == 0).all()
        return result

    @staticmethod
    def find_reply_by_user(user_id):
        """find all replies to user of user_id"""
        pass
