#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: car.py
@time: create by fanxl12 on 2020-05-24
"""
__author__ = 'fanxl12'

from flask import render_template

from . import web


@web.route('/')
def index():
    return render_template('test.html', username='王五')
