#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: index.py
@time: create by fanxl12 on 2020-05-26
"""
__author__ = 'fanxl12'
from flask import render_template

from . import web


@web.route('/')
def index():
    return render_template('index.html')