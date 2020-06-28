from flask import session


def flatten_query_result(result):
    """convert SQLAlchemy query result to list of dicts
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
