#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: user.py
@time: create by fanxl12 on 2020-05-24
"""
__author__ = 'fanxl12'

from flask import request, render_template, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user

from . import web
from ..forms.user import RegisterForm, LoginForm, EmailForm
from ..models.base import db
from ..models.user import User


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        return redirect('/')
    return render_template('user/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember = True if request.form.get('remember') else False)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = '/'
            return redirect(next)
        else:
            flash('账号不存在或密码错误', category='login_error')
    return render_template('user/login.html', form=form)


@web.route('/user/center')
@login_required
def user_center():
    return render_template('user/center.html')


@web.route('/forget/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST' and form.validate():
        account_email = form.email.data
        user = User.query.filter_by(email=account_email).first()
        if user:
            flash('一封邮件已发送到邮箱' + account_email + '，请及时查收')
            return redirect(url_for('web.login'))
        else:
            flash('邮箱不存在，请重新输入!', category='error')
    return render_template('user/reset_password.html', form=form)


@web.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')