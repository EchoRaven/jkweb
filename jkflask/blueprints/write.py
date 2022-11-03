from flask import Blueprint, request
from models import UserInfo, ArticalInfo
from exts import db
import time
import os

bp = Blueprint('write', __name__, url_prefix='/write')

basedir = os.path.abspath(os.path.dirname(__file__)) + '\\uploads\\'


@bp.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'OPTION':
        pass
    artical = request.form.get('artical')
    title = request.form.get('title')
    uid = request.form.get('uid')
    tags = request.form.get('tags')
    # 更新用户文章数量
    try:
        user = UserInfo.query.filter_by(id=uid).first()
        atnum = user.artical_num
        user.artical_num = atnum + 1
        artical_model = ArticalInfo(uid=uid, title=title, content=artical, tags=tags)
        db.session.add(artical_model)
        db.session.commit()
        return '416'
    except:
        return '417'


@bp.route('/add_image', methods=['GET', 'POST'])
def add_image():
    if request.method == 'OPTION':
        pass
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    file = request.files.get('image')
    filename = str(request.form.get('uid')) + str(request.form.get('title')) + str(int(time.time()))
    savepath = basedir + filename
    file.save(savepath)
    print('http://127.0.0.1:5000/write/static/'+filename)
    return 'http://127.0.0.1:5000/write/static/'+filename


@bp.route('/static/<filename>')
def get_filename(filename):
    with open(basedir + filename, 'rb') as f:
        return f.read()
