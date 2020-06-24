from flask import Flask, render_template, session, request, url_for, redirect
from hashlib import md5

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/')
def hello():
    # if session.get('username'):
    return render_template('index.html', article_count=3)
    # else:
    # return 'please login' + session.get('username')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'mahay' and password == md5(b'123').hexdigest():
        session['isLogin'] = 'true'
        session['username'] = 'test'
        return 'success'
    else:
        return 'fail'


@app.route('/logout')
def logout():
    # 注销后仍重定向到之前页面
    from_url = request.args.get('from')
    session.clear()
    return redirect(from_url)


if __name__ == '__main__':
    from model import Session, User

    session = Session()
    print(session.query(User).first().update_time)
    app.run(debug=True)
