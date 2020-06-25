from .database import Base, db


class User(Base):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.CHAR(32))
    avatar = db.Column(db.String(50), nullable=False, server_default=db.text("'default.png'"))
    email = db.Column(db.String(50))
    role = db.Column(db.String(10), nullable=False, server_default=db.text("'user'"))

    @staticmethod
    def find_by_username(username):
        result = User.query.filter_by(username=username).all()
        return result

    @staticmethod
    def find_by_id(user_id):
        result = User.query.filter_by(user_id=user_id).all()
        return result

    @staticmethod
    def do_register(username, nickname, password):
        user = User(username=username, nickname=nickname, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def change_nickname(user_id, nickname):
        """change user's nickname"""
        result = User.query.filter_by(user_id=user_id).first()
        result.nickname = nickname
        db.session.commit()
        return result
