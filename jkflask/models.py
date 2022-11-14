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
    artical_num = db.Column(db.Integer, default=0)
    headshot = db.Column(db.String(100), nullable=True, unique=False, default='http://127.0.0.1:5000/user/static/base')
    tempshot = db.Column(db.String(100), nullable=True, unique=False, default='http://127.0.0.1:5000/user/static/base')
    abstract = db.Column(db.Text(1024), nullable=False, unique=False, default='主人很懒，什么都没有写哦')

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


# 文章信息包括：主键序号，文章题目，点击量，标签，创建时间
class ArticalInfo(db.Model):
    __tablename__ = "ArticalInfo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=True, unique=False)
    clicks = db.Column(db.Integer, nullable=True, unique=False, default=0)
    tags = db.Column(db.String(200), nullable=False, unique=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    content = db.Column(db.Text(4294967295), nullable=False, unique=False, default="<!DOCTYPE html><title>hahaha</title><body><p>hahaha</p></body>")
    uid = db.Column(db.Integer, nullable=True, unique=False)
    likes = db.Column(db.Integer, nullable=True, unique=False, default=0)
    comments = db.Column(db.Integer, nullable=True, unique=False, default=0)

    def __init__(self, title, tags, content, uid):
        self.tags = tags
        self.content = content
        self.uid = uid
        self.title = title


class CommentInfo(db.Model):
    __tablename__ = "CommentInfo"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 记录用户uid
    uid = db.Column(db.Integer, nullable=True, unique=False)
    # 记录评论内容
    content = db.Column(db.Text(4294967295), nullable=False, unique=False, default="")
    # 记录点赞数量
    likes = db.Column(db.Integer, nullable=True, unique=False, default=0)
    # 记录自己的父节点是谁(父节点是谁同时可以决定是谁发给谁的)(父节点记录的是头像的id)
    fa = db.Column(db.Integer, nullable=True, unique=False, default=0)
    # 记录评论所属的文章的序号
    artid = db.Column(db.Integer, nullable=True, unique=False, default=0)
    # 评论发布时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 评论对象
    toid = db.Column(db.Integer, nullable=True, unique=False, default=0)

    def __init__(self, uid, content, fa, artid, toid):
        self.content = content
        self.uid = uid
        self.artid = artid
        self.fa = fa
        self.toid = toid


