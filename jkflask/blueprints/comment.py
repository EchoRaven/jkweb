from flask import Blueprint, request
from models import ArticalInfo, CommentInfo, UserInfo
import json
from exts import db

bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/get_comment', methods=['GET', 'POST'])
def get_comment():
    if request.method == 'OPTION':
        pass
    artid = request.form.get('artid')
    all_comment = CommentInfo.query.filter_by(artid=artid)
    info = {}
    info['id'] = []
    info['uid'] = []
    info['content'] = []
    info['likes'] = []
    info['fa'] = []
    info['create_time'] = []
    info['toid'] = []
    for ac in all_comment:
        info['id'].append(ac.id)
        info['uid'].append(ac.uid)
        info['content'].append(ac.content)
        info['likes'].append(ac.likes)
        info['fa'].append(ac.fa)
        info['create_time'].append(str(ac.create_time))
        info['toid'].append(ac.toid)
    info['code'] = '422'
    return json.dumps(info, ensure_ascii=False)


@bp.route('/sent_comment', methods=['GET', 'POST'])
def sent_comment():
    if request.method == 'OPTION':
        pass
    artid = request.form.get('artid')
    uid = request.form.get('uid')
    fa = request.form.get('fa')
    id = request.form.get('id')
    cid = request.form.get('cid')
    content = request.form.get('content')
    # 创建一个新的comment
    if fa == '0':
        cmodel = CommentInfo(artid=artid, fa=id, content=content, uid=uid, toid=cid)
        db.session.add(cmodel)
        db.session.commit()
    else:
        cmodel = CommentInfo(artid=artid, fa=fa, content=content, uid=uid, toid=cid)
        db.session.add(cmodel)
        db.session.commit()
    return '424'


@bp.route('/get_sender', methods=['GET', 'POST'])
def get_headshot():
    info = {}
    if request.method == 'OPTION':
        pass
    uid = request.form.get('uid')
    try:
        user = UserInfo.query.filter_by(id=uid).first()
        info['headshot'] = user.headshot
        info['username'] = user.username
    except:
        info['headshot'] = 'http://127.0.0.1:5000/user/static/base'
        info['username'] = "未登录"
    return json.dumps(info, ensure_ascii=False)
