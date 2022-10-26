from flask import Blueprint, request
from models import ArticalInfo
from sqlalchemy import desc
import json

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
        for i in range(10):
            try:
                info['arts'].append(li[i].id)
                info['title'].append(li[i].title)
            except:
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
    try:
        amodel = ArticalInfo.query.filter_by(id=index).first()
        info['content'] = amodel.content
        info['code'] = '414'
    except:
        info['code'] = '415'
    return json.dumps(info, ensure_ascii=False)




