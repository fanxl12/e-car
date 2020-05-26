#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: email.py
@time: create by fanxl12 on 2020-05-26
"""
__author__ = 'fanxl12'

from app import mail
from threading import Thread
from flask import current_app, render_template
from flask_mail import Message


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message('[E-car]' + ' ' + subject,
                  sender=app.config['MAIL_USERNAME'], recipients=[to])
    # msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
