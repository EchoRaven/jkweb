from flask import Blueprint

bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/')
def login():
    return '首页'

