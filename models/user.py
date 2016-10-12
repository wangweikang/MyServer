import os

from . import ReprMixin
from . import db


class User(db.Model, ReprMixin):
    # 类的属性就是数据库表的字段
    # 这些都是内置的 __tablename__ 是表名
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    qq = db.Column(db.String())
    email = db.Column(db.String())
    signature = db.Column(db.String())

    credit = db.Column(db.Integer, default=100)
    created_time = db.Column(db.Integer)
    # 
    topics = db.relationship('Topic', backref='user')
    comments = db.relationship('Comment', backref='user')

    def __init__(self, form):
        super(User, self).__init__()
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.email = form.get('email', '')
        self.signature = form.get('signature', '')
        self.qq = form.get('qq', '')


    def validate_auth(self, form):
        username = form.get('username', '')
        password = form.get('password', '')
        username_equals = self.username == username
        password_equals = self.password == password
        return username_equals and password_equals

    def update(self, form):
        print('user.update, ', form)
        self.password = form.get('password', self.password)

    # 验证注册用户的合法性的
    def valid(self):
        pass
