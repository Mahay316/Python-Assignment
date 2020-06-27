from common import flatten_query_result
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
    if not (msg_id and content and reply_to and reply_to_id):
        return 'invalid'

    try:
        Comment.insert_comment(session.get('user_id'), msg_id, content, reply_to, reply_to_id)
        Message.increase_reply_count(msg_id)
        return 'success'
    except IOError as e:
        print(e)
        return 'fail'


# AJAX interface
@comment.route('/comment/<int:msg_id>-<int:page>')
def get_comment(msg_id, page):
    """return certain page of comments of message msg_id"""
    res = flatten_query_result(Comment.find_original_comment(msg_id, page * 10, 10))
    for c in res:
        c['reply_list'] = flatten_query_result(Comment.find_reply_by_comment(c['comment_id']))

    return jsonify(res)
