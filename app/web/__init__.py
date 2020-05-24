#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: __init__.py.py
@time: create by fanxl12 on 2020-05-24
"""
__author__ = 'fanxl12'

from flask import Blueprint

# 实例化蓝图
web = Blueprint('web', __name__)

# 实现模块下多接口的注册
from app.web import car
from app.web import user
