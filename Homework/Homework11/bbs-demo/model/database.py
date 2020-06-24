from sqlalchemy import Column, DateTime, text, create_engine
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {'mysql_engine': 'InnoDB'}

    create_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "bbs"
USERNAME = "root"
PASSWORD = "mahay"
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4" \
    .format(username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE)

Base = declarative_base(cls=Base)  # 表模型基类
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)  # Session类，当需要进行数据库操作时需要实例化
