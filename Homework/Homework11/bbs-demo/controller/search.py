# controller responsible for searching
from common import flatten_single, flatten_double
from flask import Blueprint, render_template, jsonify, request
from model import User, Message

search = Blueprint('search', __name__, template_folder='templates')


@search.route('/search')
def get_search_page():
    return render_template('search.html')


# AJAX interface
@search.route('/search/<int:page>')
def do_search(page):
    action = request.args.get('action')
    keyword = request.args.get('keyword')

    res = []
    count = 0
    if action == 'message':
        # fuzzy search messages
        res = flatten_double(Message.fuzzy_search('%' + keyword + '%', page * 10, 10))
        count = (Message.count_fuzzy_result('%' + keyword + '%') - 1) // 10 + 1
    elif action == 'user':
        # fuzzy search users
        res = flatten_single(User.fuzzy_search('%' + keyword + '%', page * 10, 10))
        count = (User.count_fuzzy_result('%' + keyword + '%') - 1) // 10 + 1
    return jsonify([count, res])
