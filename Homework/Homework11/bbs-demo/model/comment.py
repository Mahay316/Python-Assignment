from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text, text
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.orm import relationship
from .database import Base


class Comment(Base):
    __tablename__ = 'comment'

    comment_id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.user_id'), index=True)
    message_id = Column(ForeignKey('message.message_id'), index=True)
    content = Column(Text)
    reply_to = Column(Integer, nullable=False)
    hidden = Column(BIT(1), nullable=False)

    message = relationship('Message')
    user = relationship('User')