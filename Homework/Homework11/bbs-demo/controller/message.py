# controller responsible for posting/updating/deleting message
from common import type_to_str
from flask import Blueprint, request, session, render_template, abort
from model import Message

message = Blueprint('message', __name__, template_folder='templates')


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
        msg_id = Message.insert_message(msg_type, headline, content, drafted)
        return str(msg_id)
    except IOError:
        return 'failed'


@message.route('/message/detail/<int:message_id>')
def msg(message_id):
    try:
        result = Message.find_by_id(message_id)
        if len(result) != 1:
            # if length == 0, then message doesn't exist
            # if length > 1, then the Database integrity is corrupted
            abort(404)
    except IOError as e:
        print(e)
        abort(500)

    # increase message's read count by 1
    Message.increase_read_count(message_id)
    result = result[0]
    return render_template('message-detail.html', msg=result[0], nickname=result[1],
                           msg_type=type_to_str(result[0].type))
