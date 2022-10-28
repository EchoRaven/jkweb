from flask import Blueprint, request
from models import ArticalInfo
from sqlalchemy import desc
import json
from exts import db

bp = Blueprint('home', __name__, url_prefix='/')


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
            if cnt >= 10:
                break
    except:
        info['code'] = '411'
        info['arts'] = []
        info['title'] = []
    print(info['arts'])
    return json.dumps(info, ensure_ascii=False)


@bp.route('/content', methods=['GET', 'POST'])
def get_content():
    if request.method == 'OPTION':
        pass
    index = request.form.get('id')
    info = {}
    info['content'] = ''
    info['code'] = ''
    try:
        amodel = ArticalInfo.query.filter_by(id=index).first()
        amodel.clicks = amodel.clicks + 1
        db.session.commit()
        info['content'] = amodel.content
        info['code'] = '414'
    except:
        info['code'] = '415'
    return json.dumps(info, ensure_ascii=False)




