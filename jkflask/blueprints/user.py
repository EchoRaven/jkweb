from flask import Blueprint, request
from exts import mail, db
from flask_mail import Message
import random
from forms import RegisterForm, LoginForm, EmailForm
from models import UserInfo, EmailInfo
import json
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('user', __name__, url_prefix='/user')
mdict = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


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

