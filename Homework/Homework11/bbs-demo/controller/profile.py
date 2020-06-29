# controller responsible for manipulating user's profile
from flask import Blueprint, request, session, render_template
from model import User, Comment, Message

profile = Blueprint('profile', __name__)


@profile.route('/profile', methods=['GET'])
def get_profile():
    if session.get('isLogin') != 'true':
        return 'permission-denied'

    try:
        result = User.find_by_id(session.get('user_id'))
        msg_count = Message.count_user_message(session.get('user_id'))
        comment_count = Comment.count_self_comment(session.get('user_id'))
        return render_template('profile.html', user=result[0], msg_count=msg_count, comment_count=comment_count)
    except IOError as e:
        print(e)
        return 'fail'


@profile.route('/profile/message/list/<int:page>')
def get_message_list(page):
    if session.get('isLogin') != 'true':
        return 'permission-denied'

    try:
        msg = Message.find_self_message(session.get('user_id'), page * 10, 10)
        page_count = (Message.count_user_message(session.get('user_id')) - 1) // 10 + 1
        statistics = Message.get_statistics(session.get('user_id'))
        return render_template('profile-message-list.html', result=msg, page_count=page_count,
                               curr_page=page, statistics=statistics)
    except IOError as e:
        print(e)
        return 'fail'


@profile.route('/profile/comment/<int:page>')
def get_comment(page):
    if session.get('isLogin') != 'true':
        return 'permission-denied'

    try:
        comments = Comment.find_self_comment(session.get('user_id'), page * 15, 15)
        page_count = (Comment.count_self_comment(session.get('user_id')) - 1) // 15 + 1
        statistics = Comment.get_statistics(session.get('user_id'))
        return render_template('profile-comment-list.html', result=comments, page_count=page_count,
                               curr_page=page, statistics=statistics)
    except IOError as e:
        print(e)
        return 'fail'


@profile.route('/profile/reply/<int:page>')
def get_reply(page):
    if session.get('isLogin') != 'true':
        return 'permission-denied'

    try:
        replies = Comment.find_reply_to(session.get('user_id'), page * 15, 15)
        page_count = (Comment.count_reply_to(session.get('user_id')) - 1) // 15 + 1
        statistics = Comment.get_statistics(session.get('user_id'))
        return render_template('profile-reply-list.html', result=replies, page_count=page_count,
                               curr_page=page, statistics=statistics)
    except IOError as e:
        print(e)
        return 'fail'


@profile.route('/profile', methods=['PUT'])
def change_profile():
    new_nickname = request.form.get('nickname')
    if session.get('user_id') is not None and new_nickname is not None:
        User.change_nickname(session.get('user_id'), new_nickname)
        return 'success'
    else:
        return 'invalid'
