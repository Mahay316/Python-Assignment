# controller responsible for posting/updating/deleting message
from flask import Blueprint, request, session, render_template, abort
from model import Message

message = Blueprint('message', __name__, template_folder='templates')


@message.route('/message', methods=['POST'])
def post_message():
    msg_type = request.form.get('type')
    headline = request.form.get('headline')
    content = request.form.get('content')
    drafted = bool(request.form.get('drafted'))

    # verbose check for security purpose, actually not necessary
    if session.get('user_id') is None:
        return 'permission_denied'

    if not (msg_type and headline and content and drafted):
        return 'invalid'

    try:
        msg_id = Message.insert_message(msg_type, headline, content, drafted)
        return str(msg_id)
    except IOError:
        return 'failed'


@message.route('/message/detail/<int:message_id>')
def msg(message_id):
    result = Message.find_message_by_id(message_id)
    if len(result) == 1:
        result = result[0]
        return render_template('message-detail.html')
    else:
        # if length == 0, then message doesn't exist
        # if length > 1, then the Database integrity is corrupted
        abort(404)
