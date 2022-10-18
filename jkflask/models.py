from exts import db
from datetime import datetime


class UserInfo(db.Model):
    __tablename__ = "UserInfo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=False)
    password = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    vcode = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, username, password, email, vcode):
        self.username = username
        self.password = password
        self.email = email
        self.vcode = vcode


class EmailInfo(db.Model):
    __tablename__ = "EmailInfo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    vcode = db.Column(db.String(10), nullable=False, unique=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, email, vcode):
        self.email = email
        self.vcode = vcode

