#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: user.py
@time: create by fanxl12 on 2020-05-24
"""
__author__ = 'fanxl12'

from flask import request, render_template

from . import web
from ..forms.user import RegisterForm


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        pass
    return render_template('user/register.html', form=form)