import re

from flask import session

type_map = ['编程语言', '学习交流', '影视文学',
            '电子竞技', '体育运动', '日常闲聊']


def type_to_str(msg_type):
    """convert message type represented by integer to string"""
    return type_map[msg_type]


def get_summary(html_content, length):
    """extract text from html to generate a short summary"""
    return remove_html_tag(html_content)[:length]


def flatten_single(result):
    """convert SQLAlchemy query result whose format is [obj1, obj1, ...] to list of dicts
    [{reply1}, {reply2}, ...]
    """
    res = []
    for u in result:
        tmp = {
            'create_time': u.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            'update_time': u.update_time.strftime('%Y-%m-%d %H:%M:%S'),
        }
        for k, v in u.__dict__.items():
            if not (k.startswith('_sa_instance_state') or k in tmp):
                tmp[k] = v
        res.append(tmp)
    return res


def flatten_double(result):
    """convert SQLAlchemy query result whose format is [(obj1, obj2), (obj1, obj2), ...] to list of dicts
    [{reply1}, {reply2}, ...]
    """
    res = []
    for c, u in result:
        tmp = {
            'create_time': c.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            'update_time': c.update_time.strftime('%Y-%m-%d %H:%M:%S'),
            'is_owner': c.user_id == session.get('user_id')
        }
        for k, v in c.__dict__.items():
            if not (k.startswith('_sa_instance_state') or k in tmp):
                tmp[k] = v
        for k, v in u.__dict__.items():
            if not (k.startswith('_sa_instance_state') or k in tmp):
                tmp[k] = v
        if 'content' in tmp:
            # prevent html tag from disturbing display
            tmp['content'] = remove_html_tag(tmp['content'])
        if 'type' in tmp:
            # convert type number to readable type name
            tmp['type'] = type_to_str(tmp['type'])
        res.append(tmp)
    return res


def save_session(user):
    # store login info
    session['isLogin'] = 'true'
    session['user_id'] = user.user_id
    session['username'] = user.username
    session['nickname'] = user.nickname
    session['avatar'] = user.avatar
    session['role'] = user.role


def startsWithList(string: str, matchList: list) -> bool:
    for s in matchList:
        if string.startswith(s):
            return True
    return False


def endsWithList(string: str, matchList: list) -> bool:
    for s in matchList:
        if string.endswith(s):
            return True
    return False


def remove_html_tag(html_content):
    """remove all html tags in html_content"""
    html_content = str(html_content)
    return re.sub('<.+?>', '', html_content)
