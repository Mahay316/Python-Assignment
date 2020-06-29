from common import save_session, get_summary, type_to_str
from flask import Flask, session, request, render_template
from controller import auth, ueditor, message, comment
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
                save_session(result[0])


# @app.before_request
# def verify_login():
#     print(request.path)
#     """verify requests that need login"""
#     # ignore pages don't need login
#     if request.path in ['/login', '/register', '/', '/index']:
#         return None
#     if session.get('isLogin') is None:  # 没有登录就自动跳转到登录页面去
#         return redirect('/login?from=' + request.path)


@app.errorhandler(404)
def page_not_found(err):
    return render_template('error-404.html')


@app.route('/test')
def get_test():
    return render_template('test.html')


# register function for Jinja
app.jinja_env.globals.update(get_summary=get_summary)
app.jinja_env.globals.update(type_to_str=type_to_str)

if __name__ == '__main__':
    app.app_context().push()
    init_db(app)

    app.register_blueprint(auth)
    app.register_blueprint(ueditor)
    app.register_blueprint(message)
    app.register_blueprint(comment)
    app.run(debug=True)
