"""
 Created by ldh on 18-12-3
"""
from flask import current_app

from app import login_manager
from app.models.base import Base, db
from itsdangerous import JSONWebSignatureSerializer as Serializer

__author__ = "ldh"

from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, Base):
    # __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    # 昵称
    nickname = Column(String(24), nullable=False)
    # 手机号
    phone_number = Column(String(18), unique=True)
    # 密码
    _password = Column('password', String(128), nullable=False)
    # 邮箱
    email = Column(String(50), unique=True, nullable=False)

    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        # 密码加密校验
        return check_password_hash(self._password, raw)

    # def get_id(self):  # flask_login库使用, 继承UserMixin即可省略此函数定义
    #     return self.id

    # 重置密码时将id加密编码为token, 使用itsdangerous库
    def generate_token(self, expiration='600'):
        """
        from itsdangerous import JSONWebSignatureSerializer as Serializer
        :param expiration: 过期时间, 这里默认600秒（必须加引号变为str）
        :return:
        """
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        # d = {'id': 23}
        # temp = s.dumps(d).decode('utf-8')
        # return temp
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password, expiration='600'):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        try:
            data = s.loads(token.encode('utf-8'))
            # data = data
        except:
            return False
        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password
        return True

    @property
    def summary(self):
        return dict(
            nickname=self.nickname,
            email=self.email
        )


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))


def get_user_list(page):
    return User.query.paginate(page, per_page=10)
