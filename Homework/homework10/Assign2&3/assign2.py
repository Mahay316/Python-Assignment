import pymysql
from datetime import datetime


class SQLCommand:
    def __init__(self, host='localhost', user='root', password='',
                 db=None, charset='UTF8MB4', cursor_class=pymysql.cursors.Cursor):
        """构造方法
        :param host: 数据库服务器地址
        :param user: 用于访问数据库的用户名
        :param password: 用户密码
        :param db: 访问的数据库名称
        :param charset: 字符集
        :param cursor_class: Cursor对象的类型，决定了返回数据的格式及SQL语句执行方式
        """
        # 创建数据库连接
        self.conn = pymysql.connect(host=host,
                                    user=user,
                                    password=password,
                                    database=db,
                                    charset=charset,
                                    cursorclass=cursor_class)
        self.cursor = self.conn.cursor()
        self._closed = False

    def close(self):
        """关闭数据库相关资源"""
        if self._closed:
            print('对象已经关闭')
        else:
            self.conn.close()
            self.cursor.close()

    # ***** with上下文管理器支持 ***** #
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('异常退出: {} {}'.format(exc_type, exc_val))
        self.close()

    # ***** CRUD相关函数 ***** #
    def create(self, content, username):
        """在bbs表中增加记录
        :param content: 发言内容
        :param username: 发言人
        :return: 受影响的行数量
        """
        if not (isinstance(content, str) and isinstance(username, str)):
            print(f'参数类型错误，content应为str实为{type(content)}')
            print(f'username应为str实为{type(username)}')
            return 0

        # id、time由DBMS自动生成，is_delete字段默认为0
        sql_insert = 'INSERT INTO `bbs` (`content`, `username`) VALUES (%s, %s)'
        try:
            self.cursor.execute(sql_insert, (content, username))
            self.conn.commit()
        except pymysql.Error as e:
            print('插入操作由于错误{}而终止'.format(e))
            self.conn.rollback()  # 回滚
            return 0

        return self.cursor.rowcount

    def retrieve(self, msg_id=None, content=None, username=None, time=None, is_delete=None):
        """根据指定条件查询bbs表中的记录，未传入的参数不会作为查询条件
        :return: 查询到的记录，未查询到或出现错误返回空列表
        """
        sql_select = 'SELECT * FROM `bbs`'
        param_list = []  # 查询参数
        first = True  # 第一个参数前需要插入WHERE关键字，其他参数前需要加入AND关键字

        # 构造查询式
        if isinstance(msg_id, int):
            sql_select += ' WHERE `id` = %s'
            param_list.append(msg_id)
            first = False
        if isinstance(content, str):
            # 由调用者确定是否使用模糊查询及通配符类型
            sql_select += ' WHERE `content` LIKE %s' if first else ' AND `content` LIKE %s'
            param_list.append(content)
            first = False
        if isinstance(username, str):
            # 由调用者确定是否使用模糊查询及通配符类型
            sql_select += ' WHERE `username` LIKE %s' if first else ' AND `username` LIKE %s'
            param_list.append(username)
            first = False
        if isinstance(time, datetime):
            # 由调用者确定是否使用模糊查询及通配符类型
            sql_select += ' WHERE `time` = %s' if first else ' AND `time` = %s'
            param_list.append(time.strftime('%Y-%m-%d %H:%M:%S'))  # 转换成MySQL兼容的时间格式
            first = False
        if isinstance(is_delete, bool):
            # 由调用者确定是否使用模糊查询及通配符类型
            sql_select += ' WHERE `is_delete` = %s' if first else ' AND `is_delete` = %s'
            param_list.append(int(is_delete))

        try:
            self.cursor.execute(sql_select, param_list)
            return self.cursor.fetchall()
        except pymysql.Error as e:
            print('查询操作由于错误{}而终止'.format(e))
            return []

    def update(self, msg_id, new_content):
        """更新bbs表中的指定记录，更新记录的content字段，保持其他字段不变
        :param msg_id: 待更新记录的id
        :param new_content: 更新的留言内容
        :return: 受影响的行数量
        """
        if not (isinstance(msg_id, int) and isinstance(new_content, str)):
            print(f'参数类型错误，msg_id应为int实为{type(msg_id)}')
            print(f'new_content应为str实为{type(new_content)}')
            return 0

        sql_update = 'UPDATE `bbs` SET `content` = %s WHERE `id` = %s'
        try:
            self.cursor.execute(sql_update, (new_content, msg_id))
            self.conn.commit()
        except pymysql.Error as e:
            print('更新操作由于错误{}而终止'.format(e))
            self.conn.rollback()  # 回滚
            return 0

        return self.cursor.rowcount

    def delete(self, msg_id, permanent_delete=False):
        """删除bbs表中的指定记录
        :param msg_id: 待删除记录的id
        :param permanent_delete 是否彻底删除，临时删除只将记录的is_delete字段置1
        :return: 受影响的行数量
        """
        if not isinstance(msg_id, int):
            print(f'参数类型错误，msg_id应为int实为{type(msg_id)}')
            return 0

        if permanent_delete:
            sql_delete = 'DELETE FROM `bbs` WHERE `id` = %s'
        else:
            sql_delete = 'UPDATE `bbs` SET `is_delete` = 1 WHERE `id` = %s'

        try:
            self.cursor.execute(sql_delete, (msg_id,))
            self.conn.commit()
        except pymysql.Error as e:
            print('删除操作由于错误{}而终止'.format(e))
            self.conn.rollback()  # 回滚
            return 0

        return self.cursor.rowcount


if __name__ == '__main__':
    with SQLCommand(password='mahay', db='assign', cursor_class=pymysql.cursors.DictCursor) as command:
        # 插入记录
        command.create('Does anyone familiar with PHP?', 'Mahay')
        command.create('我在学Python', '李四')
        command.create('Hi Everybody!', 'Peter')
        command.create('中文测试', 'John')

        # 查询记录，并删除
        for instance in command.retrieve(username='李四'):
            print(instance)
            command.delete(instance['id'], permanent_delete=True)

        # 更新记录
        command.update(5, 'Does anyone familiar with PHP or Python?')
