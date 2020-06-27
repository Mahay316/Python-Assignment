from sqlalchemy.dialects.mysql import BIT

from .database import Base, db


class Comment(Base):
    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.user_id'), index=True)
    message_id = db.Column(db.ForeignKey('message.message_id'), index=True)
    content = db.Column(db.Text)
    reply_to = db.Column(db.Integer, nullable=False)
    reply_to_id = db.Column(db.ForeignKey('user.user_id'), index=True)
    hidden = db.Column(BIT(1), nullable=False)

    message = db.relationship('Message')
    user1 = db.relationship('User', foreign_keys=[user_id])
    user2 = db.relationship('User', foreign_keys=[reply_to_id])

    @staticmethod
    def find_original_comment(msg_id, offset, length):
        """return all comments of message msg_id
        this static method also prepares for comments pagination
        """
        pass

    @staticmethod
    def find_reply_by_comment(reply_to):
        """find replies to a certain comment"""
        pass

    @staticmethod
    def find_reply_by_user(user_id):
        """find all replies to user of user_id"""
        pass
