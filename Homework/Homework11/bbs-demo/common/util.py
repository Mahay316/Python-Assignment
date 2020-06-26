import re

from flask import session

type_map = ['编程语言', '学习交流', '影视文学',
            '电子竞技', '体育运动', '日常闲聊']


def type_to_str(msg_type):
    """convert message type represented by integer to string"""
    return type_map[msg_type]


def save_session(user):
    # store login info
    session['isLogin'] = 'true'
    session['user_id'] = user.user_id
    session['username'] = user.username
    session['nickname'] = user.nickname
    session['avatar'] = user.avatar
    session['role'] = user.role


def get_summary(html_content, length):
    """extract text from html to generate a short summary"""
    # remove HTML tags
    summary = re.sub('<.+?>', '', html_content)
    return summary[:length]
