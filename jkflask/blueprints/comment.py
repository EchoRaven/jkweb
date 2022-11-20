from flask import Blueprint, request
from models import ArticalInfo, CommentInfo, UserInfo
import json
from exts import db

bp = Blueprint('comment', __name__, url_prefix='/comment')


def split_arr(arr: str):
    return arr.split(',')


def combine_arr(arr):
    res = ""
    for (i, index) in arr:
        if index != 0:
            res += ','
        res += i
    return res



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
    info['likes_uid'] = []
    for ac in all_comment:
        info['id'].append(ac.id)
        info['uid'].append(ac.uid)
        info['content'].append(ac.content)
        info['likes'].append(ac.likes)
        info['fa'].append(ac.fa)
        info['create_time'].append(str(ac.create_time))
        info['toid'].append(ac.toid)
        info['likes_uid'].append(split_arr(ac.likes_uid))
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


@bp.route('/point_likes', methods=['GET', 'POST'])
def point_likes():
    if request.method == 'OPTION':
        pass
    choose = request.form.get('choose')
    uid = request.form.get('uid')
    id = request.form.get('id')
    comment = CommentInfo.query.filter_by(id=id).first()
    if choose == 'true':
        comment.likes += 1
        if comment.likes != 1:
            comment.likes_uid += ','
        comment.likes_uid += uid
    else:
        comment.likes -= 1
        newli = []
        for u in comment.likes_uid:
            if u != uid:
                newli.append(u)
        comment.likes_uid = combine_arr(newli)
    db.session.commit()
    return '426'
