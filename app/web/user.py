#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: user.py
@time: create by fanxl12 on 2020-05-24
"""
__author__ = 'fanxl12'

from . import web


@web.route('/register', methods=['GET', 'POST'])
def register():
    pass
