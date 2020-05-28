from assign3_config import DB_URL

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Text, String, DateTime, Boolean
from sqlalchemy import text

from datetime import datetime

Base = declarative_base()


class BBS(Base):
    # 映射的表名
    __tablename__ = 'bbs'

    # 列信息
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    username = Column(String(255))
    time = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    is_delete = Column(Boolean, server_default=text('0'))

    def __repr__(self):
        return "<BBS(id='%s', content='%s', username='%s', time='%s', is_delete='%s')>" % (
            self.id, self.content, self.username, self.time, self.is_delete)


class SQLCommand:
    def __init__(self, print_info=False):
        """构造方法
        :param print_info: 是否输出调试信息（构造的SQL语句）
        """
        self.engine = create_engine(DB_URL, echo=print_info)
        # 一个类的实例使用一个Session对象
        self.session = sessionmaker(bind=self.engine)()

    def create(self, content, username):
        """在bbs表中增加记录
        :param content: 发言内容
        :param username: 发言人
        """
        if not (isinstance(content, str) and isinstance(username, str)):
            print(f'参数类型错误，content应为str实为{type(content)}')
            print(f'username应为str实为{type(username)}')

        self.session.add(BBS(content=content, username=username))
        self.session.commit()  # 提交事务

    def retrieve(self, msg_id=None, content=None, username=None, time=None, is_delete=None, rogue=True):
        """根据指定条件查询bbs表中的记录，未传入的参数不会作为查询条件
        :param msg_id: 留言记录的id
        :param content: 留言内容
        :param username: 用户名
        :param time: 留言时间
        :param is_delete: 是否删除（临时删除标记）
        :param rogue: 是否对content和username进行模糊查询
        :return: 查询到的记录对应的BBS对象元组，未查询到返回空列表
        """
        query_obj = self.session.query(BBS)
        if isinstance(msg_id, int):
            query_obj = query_obj.filter_by(id=msg_id)
        if isinstance(content, str):
            query_obj = query_obj.filter(BBS.content.ilike(content))\
                if rogue else query_obj.filter_by(content=content)
        if isinstance(username, str):
            query_obj = query_obj.filter(BBS.username.ilike(username))\
                if rogue else query_obj.filter_by(username=username)
        if isinstance(time, datetime):
            query_obj = query_obj.filter_by(time=time)
        if isinstance(is_delete, bool):
            query_obj = query_obj.filter_by(is_delete=is_delete)

        return query_obj.all()

    def update(self, msg_id, new_content):
        """更新bbs表中的指定记录，更新记录的content字段，保持其他字段不变
        :param msg_id: 待更新记录的id
        :param new_content: 更新的留言内容
        :return 实际更新了内容返回True，否则返回False
        """
        if not (isinstance(msg_id, int) and isinstance(new_content, str)):
            print(f'参数类型错误，msg_id应为int实为{type(msg_id)}')
            print(f'new_content应为str实为{type(new_content)}')

        # 若按msg_id查到的记录多于一条，则数据出现问题，抛出异常
        res = self.session.query(BBS).filter_by(id=msg_id).one_or_none()
        if res is not None:
            res.content = new_content
            self.session.add(res)
            self.session.commit()
            return True
        return False

    def delete(self, msg_id, permanent_delete=False):
        """删除bbs表中的指定记录
        :param msg_id: 待删除记录的id
        :param permanent_delete 是否彻底删除，临时删除只将记录的is_delete字段置1
        :return: 实际修改了表内容返回True，否则返回False
        """
        if not isinstance(msg_id, int):
            print(f'参数类型错误，msg_id应为int实为{type(msg_id)}')
            return 0

        res = self.session.query(BBS).filter_by(id=msg_id).one_or_none()
        if res is not None:
            if permanent_delete:
                self.session.delete(res)
            else:
                res.is_delete = True
                self.session.add(res)
            self.session.commit()
            return True
        return False


if __name__ == '__main__':
    # 创建SQLCommand对象对bbs表执行SQL操作
    # 打开调试输出模式
    sql = SQLCommand(True)

    # 插入记录
    sql.create('Python is great!', 'Mahay')
    sql.create('大家好', '张三')
    sql.create('Hi there.', 'Peter')
    sql.create('How is it going, guys?', 'Peter')

    # 查询记录，并删除
    for instance in sql.retrieve(username='Peter', rogue=False):
        print(instance)
        sql.delete(instance.id)

    # 更新记录
    sql.update(2, '大家好啊 :-)')
