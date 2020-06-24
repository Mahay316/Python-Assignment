from sqlalchemy import CHAR, Column, DateTime, Integer, String, text
from .database import Base


class User(Base):
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    nickname = Column(String(50), nullable=False)
    password = Column(CHAR(32))
    avatar = Column(String(50), nullable=False, server_default=text("'default.png'"))
    email = Column(String(50))
    role = Column(String(10), nullable=False, server_default=text("'user'"))
