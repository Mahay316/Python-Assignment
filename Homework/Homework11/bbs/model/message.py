from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.dialects.mysql import BIT, MEDIUMTEXT, TINYINT
from sqlalchemy.orm import relationship
from .database import Base


class Message(Base):
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

    user = relationship('User')
