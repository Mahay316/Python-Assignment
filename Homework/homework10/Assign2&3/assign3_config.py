# SQLAlchemy连接数据库的配置信息

HOST_NAME = 'localhost'
PORT = '3306'
DATABASE = 'assign'
USER_NAME = 'root'
PASSWORD = 'mahay'

DB_URL = f'mysql+mysqlconnector://{USER_NAME}:{PASSWORD}@{HOST_NAME}:{PORT}/{DATABASE}?charset=utf8'
