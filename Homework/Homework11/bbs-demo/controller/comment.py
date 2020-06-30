from common import flatten_double
from flask import Blueprint, jsonify, session, request
from model import Comment, Message

comment = Blueprint('comment', __name__)


@comment.route('/comment', methods=['POST'])
def post_comment():
    """post new comment"""
    if session.get('user_id') is None:
        return 'permission-denied'

    msg_id = request.form.get('msg_id')
    content = request.form.get('content')
    reply_to = request.form.get('reply_to')
    reply_to_id = request.form.get('reply_to_id')
    # parameter check
    if not (msg_id and content and reply_to and reply_to_id) or len(content) <= 0:
        return 'invalid'

    try:
        Comment.insert_comment(session.get('user_id'), msg_id, content, reply_to, reply_to_id)
        Message.increase_reply_count(msg_id)
        return 'success'
    except IOError as e:
        print(e)
        return 'fail'


@comment.route('/comment/toggle', methods=['POST'])
def hide_comment():
    # hiding comments requires login
    if session.get('isLogin') != 'true':
        return 'permission-denied'

    hide = bool(int(request.form.get('toggle')))
    comment_id = request.form.get('comment_id')
    result = Comment.find_by_id(comment_id)

    if len(result) != 1:
        return 'invalid'
    elif result[0].user_id != session.get('user_id'):
        return 'permission-denied'
    else:
        # the comment exists and current user has permission
        try:
            if hide:
                Comment.hide_comment(comment_id)
            else:
                Comment.show_comment(comment_id)
            return 'success'
        except IOError as e:
            print(e)
            return 'fail'


# AJAX interface
@comment.route('/comment/<int:msg_id>-<int:page>')
def get_comment(msg_id, page):
    """return certain page of comments of message msg_id"""
    res = flatten_double(Comment.find_original_comment(msg_id, page * 10, 10))
    # the number of pages of comments, 10 comments per page
    count = (Comment.count_original_comment(msg_id) - 1) // 10 + 1
    for c in res:
        c['reply_list'] = flatten_double(Comment.find_reply_by_comment(c['comment_id']))

    return jsonify((count, res))
