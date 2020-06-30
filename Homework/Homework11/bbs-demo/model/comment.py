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
    def find_original_comment(msg_id, offset, length):
        """return all comments of message msg_id
        this static method also prepares for comments pagination
        """
        result = db.session.query(Comment, User).join(User, User.user_id == Comment.user_id) \
            .filter(Comment.message_id == msg_id, Comment.hidden == 0, Comment.reply_to == 0) \
            .order_by(Comment.comment_id.desc()).limit(length).offset(offset).all()
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
    def show_comment(comment_id):
        """show the comment of the certain comment_id"""
        result = Comment.query.filter_by(comment_id=comment_id).first()
        if result is not None:
            result.hidden = 0
            db.session.commit()
        return result.comment_id

    @staticmethod
    def count_original_comment(msg_id):
        """return the number of comments of message msg_id"""
        return Comment.query \
            .filter(Comment.message_id == msg_id, Comment.hidden == 0, Comment.reply_to == 0) \
            .count()

    @staticmethod
    def get_statistics(self_id):
        """return basic statistics of author's(self_id) comments"""
        total = Comment.query.filter_by(user_id=self_id).all()
        result = [0, 0, 0, 0]
        for m in total:
            result[0] += 1
            if m.hidden:
                result[1] += 1
            if m.reply_to == 0:
                result[2] += 1
            else:
                result[3] += 1
        return result

    @staticmethod
    def find_reply_by_comment(reply_to):
        """find replies to a certain comment"""
        # reply_to can also constraint the message that the reply belongs to
        result = db.session.query(Comment, User).join(User, User.user_id == Comment.user_id) \
            .filter(Comment.reply_to == reply_to, Comment.hidden == 0).all()
        return result

    @staticmethod
    def find_reply_to(user_id, offset, length):
        """query replies to user_id, return records from offset to offset + length"""
        result = db.session.query(Comment, User.nickname, User.avatar) \
            .join(User, User.user_id == Comment.user_id) \
            .filter(Comment.reply_to_id == user_id, Comment.hidden == 0, Comment.user_id != user_id) \
            .order_by(Comment.comment_id.desc()).limit(length).offset(offset).all()
        return result

    @staticmethod
    def count_reply_to(user_id):
        """return the number of comments that replied to user_id"""
        return Comment.query\
            .filter(Comment.reply_to_id == user_id, Comment.hidden == 0, Comment.user_id != user_id)\
            .count()

    @staticmethod
    def find_self_comment(self_id, offset, length):
        """query author's(self_id) own comments, return records from offset to offset + length"""
        result = db.session.query(Comment, User.nickname, User.avatar) \
            .join(User, User.user_id == Comment.reply_to_id) \
            .filter(Comment.user_id == self_id) \
            .order_by(Comment.comment_id.desc()).limit(length).offset(offset).all()
        return result

    @staticmethod
    def count_self_comment(self_id):
        return Comment.query.filter(Comment.user_id == self_id).count()
