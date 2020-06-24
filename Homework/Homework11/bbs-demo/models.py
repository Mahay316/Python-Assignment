# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, ForeignKey, Integer, String, Text, text
from sqlalchemy.dialects.mysql import BIT, MEDIUMTEXT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    nickname = Column(String(50), nullable=False)
    password = Column(CHAR(32))
    avatar = Column(String(50), nullable=False, server_default=text("'default.png'"))
    email = Column(String(50))
    role = Column(String(10), nullable=False, server_default=text("'user'"))
    create_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Message(Base):
    __tablename__ = 'message'

    message_id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.user_id'), index=True)
    type = Column(TINYINT, nullable=False)
    headline = Column(String(100), nullable=False)
    content = Column(MEDIUMTEXT)
    read_count = Column(Integer, nullable=False, server_default=text("'0'"))
    reply_count = Column(Integer, nullable=False, server_default=text("'0'"))
    hidden = Column(BIT(1), nullable=False)
    drafted = Column(BIT(1), nullable=False)
    recommended = Column(BIT(1), nullable=False)
    create_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    user = relationship('User')


class Comment(Base):
    __tablename__ = 'comment'

    comment_id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.user_id'), index=True)
    message_id = Column(ForeignKey('message.message_id'), index=True)
    content = Column(Text)
    reply_to = Column(Integer, nullable=False)
    hidden = Column(BIT(1), nullable=False)
    create_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    message = relationship('Message')
    user = relationship('User')
