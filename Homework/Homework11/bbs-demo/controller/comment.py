from flask import Blueprint

comment = Blueprint('comment', __name__)


# AJAX interface
@comment.route('/comment/<int:msg_id>-<int:page>')
def get_comment(msg_id, page):
    """return certain page of comments of message msg_id"""
    pass
