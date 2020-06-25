# controller responsible for responding UEditor
from flask import Blueprint, request, session, redirect, make_response, render_template

ueditor = Blueprint('ueditor', __name__, template_folder='../templates')


@ueditor.route('/uedit', methods=['GET', 'POST'])
def uedit():
    param = request.args.get('action')
    if request.method == 'GET' and param == 'config':
        return render_template('config.json')

    if request.method == 'POST' and param == 'uploadimg':
        pass
