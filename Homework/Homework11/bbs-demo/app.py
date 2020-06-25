from flask import Flask, render_template, session, request, redirect
from controller import auth, ueditor, message
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


# @app.before_request
# def verify_login():
#     print(request.path)
#     """verify requests that need login"""
#     # ignore pages don't need login
#     if request.path in ['/login', '/register', '/', '/index']:
#         return None
#     if session.get('isLogin') is None:  # 没有登录就自动跳转到登录页面去
#         return redirect('/login?from=' + request.path)
#     return None


@app.route('/editor')
def editor():
    return render_template('editor.html')


@app.route('/')
@app.route('/index')
def hello():
    return render_template('index.html', article_count=3)


if __name__ == '__main__':
    app.app_context().push()
    init_db(app)

    app.register_blueprint(auth)
    app.register_blueprint(ueditor)
    app.register_blueprint(message)
    app.run(debug=True)
