from flask import Blueprint, request
from models import ArticalInfo
from sqlalchemy import desc
import json
from exts import db

bp = Blueprint('home', __name__, url_prefix='/')


def split_arr(arr: str):
    return arr.split(',')


def combine_arr(arr):
    res = ""
    for (i, index) in arr:
        if index != 0:
            res += ','
        res += i
    return res


@bp.route('/')
def login():
    return '首页'


@bp.route('/recommand', methods=['GET', 'POST'])
def recommand():
    # 返回一个js序列
    if request.method == 'OPTION':
        pass
    info = {}
    li = ArticalInfo.query.order_by(desc(ArticalInfo.clicks))
    try:
        info['code'] = '410'
        info['arts'] = []
        info['title'] = []
        cnt = 0
        for ele in li:
            info['arts'].append(ele.id)
            info['title'].append(ele.title)
            cnt = cnt + 1
            if cnt >= 6:
                break
    except:
        info['code'] = '411'
        info['arts'] = []
        info['title'] = []
    return json.dumps(info, ensure_ascii=False)


@bp.route('/content', methods=['GET', 'POST'])
def get_content():
    if request.method == 'OPTION':
        pass
    index = request.form.get('id')
    info = {}
    info['content'] = ''
    info['code'] = ''
    info['title'] = ''
    info['clicks'] = ''
    info['likes'] = ''
    info['collect_num'] = ''
    info['collection'] = []
    try:
        amodel = ArticalInfo.query.filter_by(id=index).first()
        amodel.clicks = amodel.clicks + 1
        db.session.commit()
        info['content'] = amodel.content
        info['title'] = amodel.title
        info['clicks'] = amodel.clicks
        info['likes'] = amodel.likes
        info['likes_uid'] = split_arr(amodel.likes_uid)
        info['collect_num'] = amodel.collect_num
        info['collection'] = split_arr(amodel.collection)
        info['tags'] = amodel.tags
        info['code'] = '414'
    except:
        info['code'] = '415'
    return json.dumps(info, ensure_ascii=False)


@bp.route('/point_likes', methods=['GET', 'POST'])
def point_likes():
    if request.method == 'OPTION':
        pass
    choose = request.form.get('choose')
    uid = request.form.get('uid')
    id = request.form.get('id')
    amodel = ArticalInfo.query.filter_by(id=id).first()
    if choose == 'true':
        amodel.likes += 1
        if amodel.likes != 1:
            amodel.likes_uid += ','
        amodel.likes_uid += uid
    else:
        amodel.likes -= 1
        newli = ""
        for u in amodel.likes_uid:
            if u != uid:
                newli.append(u)
        amodel.likes_uid = newli
        if amodel.likes == 0:
            amodel.likes_uid = ""
    db.session.commit()
    return '427'

