from flask import session

type_map = ['编程语言', '编程语言', '编程语言']


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
