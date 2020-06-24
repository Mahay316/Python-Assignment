from flask import Flask, render_template, session, request
from controller import auth
from model import User, init_db

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.before_request
def auto_login():
    """automated login using cookie"""
    if session.get('isLogin') is None:
        username = request.cookies.get('username')
        password = request.cookies.get('password')
        if username is not None and password is not None:
            result = User.find_by_username(username)
            if len(result) == 1 and password == result[0].password:
                result = result[0]
                # store login info
                session['isLogin'] = 'true'
                session['user_id'] = result.user_id
                session['username'] = result.username
                session['nickname'] = result.nickname
                session['role'] = result.role


@app.route('/')
def hello():
    # if session.get('username'):
    return render_template('index.html', article_count=3)
    # else:
    # return 'please login' + session.get('username')


if __name__ == '__main__':
    app.app_context().push()
    init_db(app)

    app.register_blueprint(auth)
    app.run(debug=True)
