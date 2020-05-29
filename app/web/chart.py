#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: chart.py
@time: create by fanxl12 on 2020-05-29
"""
__author__ = 'fanxl12'

from flask import render_template
from jinja2 import Markup
from . import web
from pyecharts.charts import Bar, Line
from pyecharts import options as opts


@web.route('/bar')
def bar():
    bar = Bar()
    bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])\
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])\
        .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])\
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    return Markup(bar.render_embed())


@web.route('/car-chart')
def car_chart():
    bar = Bar()
    bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])

    line = Line()
    line.add_xaxis(['1月', '2月', '3月', '4月'])\
        .add_yaxis("电动车数量", [10, 150, 61, 10], is_connect_nones=True)\
        .set_global_opts(title_opts=opts.TitleOpts(title="电动车目录情况"))
    return render_template('car/car_chart.html', bar=Markup(bar.render_embed()), line=Markup(line.render_embed()))