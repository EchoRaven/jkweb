from flask import Blueprint, request
from exts import mail, db
from flask_mail import Message
import random
from forms import RegisterForm, LoginForm, EmailForm
from models import UserInfo, EmailInfo, ArticalInfo
import json
import os
import time
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('user', __name__, url_prefix='/user')
mdict = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
basedir = os.path.abspath(os.path.dirname(__file__)) + '\\headshot\\'


# 402是用户名或密码输入格式错误
@bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'OPTION':
        pass
    form = LoginForm(request.form)
    print(form.password.data)
    print(form.username.data)
    info = {}
    info['id'] = "-1"
    if form.validate():
        username = form.username.data
        password = form.password.data
        user = UserInfo.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                info['id'] = user.id
                info['code'] = '402'

            else:
                info['code'] = '404'
        else:
            info['code'] = '405'
    else:
        info['code'] = '403'
    return json.dumps(info, ensure_ascii=False)


@bp.route('/mail', methods=['POST', 'GET'])
def send_mail():
    if request.method == 'OPTION':
        pass
    form = EmailForm(request.form)
    if form.validate():
        email = form.email.data
        vcode = ''.join(random.sample(mdict, 4))
        print(vcode)
        print(email)
        message = Message(
            subject="jkweb验证码",
            recipients=[email],
            body="验证码为" + vcode
        )
        try:
            mail.send(message)
        except:
            return "406"
        v_exist = EmailInfo.query.filter_by(email=email).first()
        if v_exist:
            return "408"
        else:
            vmodel = EmailInfo(email=email, vcode=vcode)
            db.session.add(vmodel)
            db.session.commit()
            return "407"
    else:
        print("邮箱格式错误")
        return "409"


# 400是注册成功，401是注册失败
@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'OPTION':
        pass
    form = RegisterForm(request.form)
    if form.validate():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        vcode = form.vcode.data
        user = UserInfo(email=email, username=username, password=password, vcode=vcode)
        db.session.add(user)
        db.session.commit()
        return '400'
    else:
        return '401'


@bp.route('/post_headshot', methods=['GET', 'POST'])
def post_headshot():
    if request.method == 'OPTION':
        pass
    file = request.files.get('image')
    # 获取文件
    filename = str(request.form.get('uid')) + str(int(time.time()))
    savepath = basedir + filename
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    # 储存文件
    file.save(savepath)
    info = {}
    try:
        # 储存url
        uid = request.form.get('uid')
        # 更新用户的头像url
        user = UserInfo.query.filter_by(id=uid).first()
        user.tempshot = 'http://127.0.0.1:5000/user/static/' + filename
        db.session.commit()
        info['code'] = '418'
        info['tempshot'] = user.tempshot
        return json.dumps(info, ensure_ascii=False)
    except:
        info['code'] = '419'
        info['tempshot'] = 'http://127.0.0.1:5000/user/static/base'
        return json.dumps(info, ensure_ascii=False)


@bp.route('/static/<filename>')
def get_filename(filename):
    with open(basedir + filename, 'rb') as f:
        return f.read()


@bp.route('/get_userinfo', methods=['GET', 'POST'])
def get_headshot():
    info = {}
    if request.method == 'OPTION':
        pass
    uid = request.form.get('uid')
    try:
        user = UserInfo.query.filter_by(id=uid).first()
        info['headshot'] = user.headshot
        info['tempshot'] = user.tempshot
        info['username'] = user.username
        info['abstract'] = user.abstract
    except:
        info['headshot'] = 'http://127.0.0.1:5000/user/static/base'
        info['tempshot'] = 'http://127.0.0.1:5000/user/static/base'
        info['username'] = '未登录'
        info['abstract'] = '主人很懒，什么都没有写哦'
    return json.dumps(info, ensure_ascii=False)


@bp.route('ensure_headshot', methods=['GET', 'POST'])
def ensure_headshot():
    if request.method == 'OPTION':
        pass
    uid = request.form.get('uid')
    info = {}
    try:
        user = UserInfo.query.filter_by(id=uid).first()
        user.headshot = user.tempshot
        db.session.commit()
        info['code'] = '420'
    except:
        info['code'] = '421'
    info['headshot'] = user.headshot
    return json.dumps(info, ensure_ascii=False)


@bp.route('close_headshot', methods=['GET', 'POST'])
def close_headshot():
    if request.method == 'OPTION':
        pass
    uid = request.form.get('uid')
    info = {}
    try:
        user = UserInfo.query.filter_by(id=uid).first()
        user.tempshot = user.headshot
        db.session.commit()
        info['code'] = '420'
    except:
        info['code'] = '421'
    info['tempshot'] = user.tempshot
    return json.dumps(info, ensure_ascii=False)


@bp.route('change_abstract', methods=['GET', 'POST'])
def change_abstract():
    if request.method == 'OPTIOIN':
        pass
    uid = request.form.get('uid')
    try:
        user = UserInfo.query.filter_by(id=uid).first()
        user.abstract = request.form.get('abstract')
        db.session.commit()
        return request.form.get('abstract')
    except:
        return '主人很懒，什么都没有写哦'


@bp.route('get_all_artical', methods=['GET', 'POST'])
def get_all_artical():
    if request.method == 'OPTIOIN':
        pass
    uid = request.form.get('uid')
    info = {}
    articals = ArticalInfo.query.filter_by(uid=uid)
    info['code'] = 420
    info['title'] = []
    info['content'] = []
    info['clicks'] = []
    info['create_time'] = []
    info['likes'] = []
    info['comments'] = []
    info['tags'] = []
    for art in articals:
        print(art)
        info['title'].append(art.title)
        info['content'].append(art.content)
        info['clicks'].append(art.clicks)
        info['tags'].append(art.tags)
        info['likes'].append(art.likes)
        info['comments'].append(art.comments)
        info['create_time'].append(str(art.create_time))
    return json.dumps(info, ensure_ascii=False)
