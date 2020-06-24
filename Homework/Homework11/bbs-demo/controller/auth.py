# controller responsible for authentication and registration
from flask import Blueprint, request, session, redirect, make_response
from model import User

auth = Blueprint('auth', __name__, template_folder='../templates')


@auth.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    auto_login = request.form.get('auto_login')

    # parameter not enough
    if not (username and password):
        return 'invalid'

    # authenticate
    result = User.find_by_username(username)
    if len(result) == 1 and password == result[0].password:
        result = result[0]

        # store login info
        session['isLogin'] = 'true'
        session['user_id'] = result.user_id
        session['username'] = result.username
        session['nickname'] = result.nickname
        session['role'] = result.role

        resp = make_response('success')
        # set cookies for automated login
        if auto_login == 'true':
            # cookies' max age is 1 month
            resp.set_cookie('username', username, max_age=30*24*3600)
            resp.set_cookie('password', password, max_age=30*24*3600)
        return resp
    else:
        return 'fail'


@auth.route('/logout')
def logout():
    # redirect to previous page after logout
    from_url = request.args.get('from')
    session.clear()

    resp = redirect(from_url)
    # delete cookies for automated login
    resp.delete_cookie('username')
    resp.delete_cookie('password')

    return resp


@auth.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    nickname = request.form.get('nickname')
    password = request.form.get('password')

    # parameter not enough
    if not (username and nickname and password):
        return 'invalid'

    # username already exists
    if len(User.find_by_username(username)) > 0:
        return 'duplicated'

    User.do_register(username, nickname, password)
    return 'success'