#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: __init__.py.py
@time: create by fanxl12 on 2020-05-24
"""
__author__ = 'fanxl12'

from flask import Blueprint, render_template

# 实例化蓝图
web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


# 实现模块下多接口的注册
from app.web import car
from app.web import user
from app.web import index
from app.web import chart
