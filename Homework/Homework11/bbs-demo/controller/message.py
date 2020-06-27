# controller responsible for posting/updating/deleting message
from math import ceil

from common import type_map
from flask import Blueprint, request, session, render_template, abort
from model import Message, User

message = Blueprint('message', __name__, template_folder='templates')


@message.route('/')
@message.route('/index')
def index():
    msg_count = []
    msgs = []
    for i in range(len(type_map)):
        msg_count.append(Message.count_msg_of_type(i))
        msgs.append(Message.find_top(i, 3))
    users = User.find_new(5)
    return render_template('index.html', msgs=msgs, users=users, type_map=type_map, msg_count=msg_count)


@message.route('/message', methods=['POST'])
def post_message():
    msg_type = request.form.get('type')
    headline = request.form.get('headline')
    content = request.form.get('content')
    drafted = bool(int(request.form.get('drafted')))

    # verbose check for security purpose, actually not necessary
    if session.get('user_id') is None:
        return 'permission_denied'

    if not (msg_type and headline and content):
        return 'invalid'

    try:
        msg_id = Message.insert_message(session.get('user_id'), msg_type, headline, content, drafted)
        return str(msg_id)
    except IOError:
        return 'failed'


@message.route('/message/detail/<msg_id>')
def get_msg(msg_id):
    """get message with message id message_id"""
    try:
        users = User.find_new(5)
        result = Message.find_by_id(msg_id)
        if len(result) != 1:
            # if length == 0, then message doesn't exist
            # if length > 1, then the Database integrity is corrupted
            abort(404)
    except IOError as e:
        print(e)
        abort(500)

    # increase message's read count by 1
    Message.increase_read_count(msg_id)
    result = result[0]
    return render_template('message-detail.html', msg=result[0], users=users,
                           type_map=type_map, nickname=result[1])


@message.route('/message/list/<int:msg_type>-<int:page>')
def get_msg_list(msg_type, page):
    """get paginated message list"""
    count = ceil(Message.count_msg_of_type(msg_type) / 10)
    if msg_type >= len(type_map) or page >= count:  # request a nonexistent page
        abort(404)

    result = Message.find_limit_of_type(msg_type, page * 10, 10)
    users = User.find_new(5)
    return render_template('message-list.html', result=result, users=users, msg_type=msg_type, type_map=type_map,
                           curr_page=page, page_count=count)
