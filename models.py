from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import time
import json

app = Flask(__name__)
app.secret_key = "zheshigehsa"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db = SQLAlchemy(app)


class ModelHelper(object):
    def __repr__(self):

        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '< {} \n{} \n>\n'.format(classname, s)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Blog(db.Model, ModelHelper):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)

    user_id = db.Column(db.Integer)

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = int(time.time())
        self.comment = []

    def load_comments(self):
        self.comments = Comment.query.filter_by(weibo_id=self.id).all()


class Weibo(db.Model, ModelHelper):
    __tablename__ = 'weibos'
    # 下面是字段定义
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)
    # 定义关系
    user_id = db.Column(db.Integer)

    def __init__(self, form):
        self.content = form.get('content', '')
        self.created_time = int(time.time())
        self.comments = []

    def load_comments(self):
        self.comments = Comment.query.filter_by(weibo_id=self.id).all()


class Comment(db.Model, ModelHelper):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    create_time = db.Column(db.Integer, default=0)

    user_id = db.Column(db.Integer)
    weibo_id = db.Column(db.Integer)

    def __init__(self, form):
        self.content = form.get('content', '')
        self.create_time = int(time.time())

    def json(self):
        d = {
            'id' : self.id,
            'content' : self.content,
            'create_time' : self.created_time,
            'weibo_id' : self.weibo_id,
            'user_id' : self.user_id,
        }
        return json.dumps(d, ensure_ascii=False)

class User(db.Model, ModelHelper):
    __tablename__ = 'users'

    id = db.Colum(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    create_time = db.Column(db.Integer, default=0)

    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.create_time = int(time.time())

    def weibos(self):
        ws = Weibo.query.filter_by(user_id=self.id).all
        return ws

    def vaild(self):
        return len(self.username) > 2 and len(self.password) > 2

    def validate_login(self, u):
        return u is not None and u.username == self.username and u.password == self.password

    def change_password(self, password):
        if len(password) > 2:
            self.password = password
            self.save()
            return True
        else:
            return False


def init_db():
    db.drop_all()
    db.create_all()
    print('rebuild database')


if __name__ == '__name__':
    init_db()