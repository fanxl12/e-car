#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: car.py
@time: create by fanxl12 on 2020-05-27
"""
__author__ = 'fanxl12'

from wtforms import Form, StringField
from wtforms.validators import URL

from app.forms.base import DataRequired


class CarUrlForm(Form):
    url = StringField('网址', validators=[
        DataRequired(), URL(message='网址不符合规范')])
