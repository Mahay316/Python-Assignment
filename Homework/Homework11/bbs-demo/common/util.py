from flask import session


def save_session(user):
    # store login info
    session['isLogin'] = 'true'
    session['user_id'] = user.user_id
    session['username'] = user.username
    session['nickname'] = user.nickname
    session['avatar'] = user.avatar
    session['role'] = user.role
