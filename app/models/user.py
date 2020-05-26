#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: user.py
@time: create by fanxl12 on 2020-05-24
"""
__author__ = 'fanxl12'

from flask import current_app
from flask_login import UserMixin
from itsdangerous import Serializer
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, Boolean, Float


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False, comment='昵称')
    phone_number = Column(String(18), unique=True, comment='手机号码')
    email = Column(String(50), unique=True, nullable=False, comment='邮箱')
    active = Column(Boolean, default=False, comment='是否可用')
    integral = Column(Float, default=0, comment='积分')
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    _password = Column('password', String(100))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except Exception as e:
            return False
        user = User.query.get(data.get('id'))
        if user is None:
            return False
        user.password = new_password
        db.session.commit()
        return True


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
