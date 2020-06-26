# controller responsible for responding and configuring UEditor
from common import type_map
from flask import Blueprint, request, render_template, jsonify, session

ueditor = Blueprint('ueditor', __name__, template_folder='../templates')


@ueditor.route('/editor')
def editor():
    return render_template('editor.html', msg_type=type_map)


@ueditor.route('/uedit', methods=['GET', 'POST'])
def uedit():
    param = request.args.get('action')
    # return configuration file
    if request.method == 'GET' and param == 'config':
        return render_template('config.json')
    # upload image
    elif request.method == 'POST' and param == 'uploadimage':
        return upload_img()


def upload_img():
    img = request.files['upfile']
    filename = f'user{session.get("user_id")}_' + img.filename
    resp = {
        'url': f'/static/upload/{filename}',
        'title': filename,
        'original': filename
    }
    try:
        img.save('./static/upload/' + filename)
        resp['state'] = 'SUCCESS'
    except IOError as e:
        print(e)
        resp['state'] = 'FAIL'
    finally:
        return jsonify(resp)
