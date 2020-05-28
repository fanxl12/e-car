#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: index.py
@time: create by fanxl12 on 2020-05-26
"""
__author__ = 'fanxl12'
from flask import render_template
from sqlalchemy import func, distinct

from . import web
from ..models.base import db
from ..models.car import Car
from ..view_models.car import CarIndexModel


@web.route('/')
def index():
    model_count = Car.query.count()
    brand_count_list = db.session.query(func.count(distinct(Car.brand))).group_by(Car.brand).all()
    car = CarIndexModel()
    car.set_model_count(model_count)
    car.set_brand_count(len(brand_count_list))
    return render_template('index.html', car=car)