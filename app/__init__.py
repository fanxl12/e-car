#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: __init__.py.py
@time: create by fanxl12 on 2020-05-24
"""
__author__ = 'fanxl12'

from flask import Flask


def create_app():
    app = Flask(__name__)
    # 从模块里面加载配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprint(app)
    return app


def register_blueprint(app):
    """
    注册蓝图
    :param app:
    :return:
    """
    from app.web import web
    app.register_blueprint(web)
