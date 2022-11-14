from flask import Blueprint, request
from models import ArticalInfo
import json

bp = Blueprint('search', __name__, url_prefix='/search')


def check_tags(tagsa, tagsb):
    if tagsa == "" or tagsb == "":
        return True
    tagarra = tagsa.split(',')
    tagarrb = tagsb.split(',')
    for ta in tagarra:
        for tb in tagarrb:
            if ta == tb:
                return True
    return False


@bp.route('get_search', methods=['GET', 'POST'])
def get_search():
    if request.method == 'OPTION':
        pass
    # 获取标签与搜索信息
    tags = request.form.get('tags')
    words = request.form.get('words')
    # 先获取含有words的所有文章,然后搜索所有含有tags的文章
    artwithwords = ArticalInfo.query.filter(ArticalInfo.content.contains(words)).all()
    artres = []
    for art in artwithwords:
        if check_tags(art.tags, tags):
            artres.append(art)
    info = {}
    info['search_id'] = []
    # 同时返回文章标题
    info['search_title'] = []
    for res in artres:
        info['search_id'].append(res.id)
        info['search_title'].append(res.title)
    return json.dumps(info, ensure_ascii=False)
