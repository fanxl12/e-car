#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: car.py
@time: create by fanxl12 on 2020-05-24
"""
__author__ = 'fanxl12'

from flask import render_template, flash, request
from flask_login import login_required
from sqlalchemy import func, desc

from . import web
from ..forms.car import CarUrlForm
from ..models.base import db
from ..models.car import Car
from ..spider.car import CarHttp


@web.route('/car', methods=['GET', 'POST'])
@login_required
def get_car():
    form = CarUrlForm(request.form)
    if request.method == 'POST' and form.validate():
        car_list = CarHttp.get_car(form.url.data)
        if car_list:
            with db.auto_commit():
                db.session.add_all(car_list)
            flash('爬取' + str(len(car_list)) + '条数据')
    return render_template('get_car.html', form=form)


@web.route('/brand')
def brand_list():
    # brand_list = db.session.query(Car.brand, func.count(Car.brand)).group_by(Car.brand).order_by(
    #         desc(func.count(Car.brand))
    #     ).all()
    page = request.args.get('page', default=1, type=int)
    page_obj = db.session.query(Car.brand, func.count(Car.brand)).group_by(Car.brand).order_by(
        desc(func.count(Car.brand))
    ).paginate(page=page, per_page=10, error_out=False)
    return render_template('car/brand.html', page=page_obj)


