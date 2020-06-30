# controller responsible for searching
from flask import Blueprint, render_template

search = Blueprint('search', __name__, template_folder='templates')


@search.route('/search')
def get_search_page():
    return render_template('search.html')
