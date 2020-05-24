#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: user.py
@time: create by fanxl12 on 2020-05-24
"""
__author__ = 'fanxl12'

from werkzeug.security import generate_password_hash

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float


class User(Base):
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
