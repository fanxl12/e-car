#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: car.py
@time: create by fanxl12 on 2020-05-26
"""
__author__ = 'fanxl12'

import re

import requests
from bs4 import BeautifulSoup

from app.models.car import Car


def get_value(p):
    str = p.text if p.string == None else p.string
    return str.strip().replace(u'\xa0', '::').replace(' ', '')


def get_html(url):
    try:
        print('开始爬取:{}'.format(url))
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return None


def analysis_html(html):
    soup = BeautifulSoup(html, "html.parser")
    article_div = soup.find('div', class_='article')
    title = article_div.find('h2')
    time_element = soup.find('i', class_='icon-clock').next_sibling
    CarHttp.time = time_element.string.strip()
    CarHttp.source = get_value(title)
    for thead in soup.find_all('thead'):
        td_array = thead.find_all('td')
        for tbody in soup.find_all('tbody'):
            if get_value(td_array[3]) == '生产企业名称' and get_value(td_array[4]) == '型号':
                return get_one(tbody.find_all('tr'), 0)
            elif get_value(td_array[3]) == '型号' and get_value(td_array[4]) == '电池类型':
                return get_one(tbody.find_all('tr'), 1)
            elif get_value(td_array[3]) == '车辆型号' and get_value(td_array[4]) == '蓄电池配置':
                return get_two(tbody.find_all('tr'))


class CarHttp:
    URL = ''
    source = ''
    time = ''

    @staticmethod
    def get_car(url):
        CarHttp.URL = url
        html = get_html(url)
        return analysis_html(html)


def get_two(tr_array):
    item = {}
    car_list = []
    for tr in tr_array:
        td_array = tr.find_all('td')
        length = len(td_array)
        for i, td in enumerate(td_array):
            for index, p in enumerate(td.find_all('p')):
                if length == 8:
                    if i == 1:
                        item['brand'] = get_value(p)
                    elif i == 2:
                        item['producer'] = get_value(p)
                    elif i == 3:
                        item['model'] = get_value(p)
                    elif i == 4:
                        item['battery_type'] = get_value(p)
                    elif i == 5:
                        item['battery_math'] = get_value(p)
                    elif i == 6:
                        item['charger_type'] = get_value(p)
                    elif i == 7:
                        item['charger_company'] = get_value(p)
                        add_car(item, car_list)
                elif length == 5:
                    if i == 0:
                        item['model'] = get_value(p)
                    elif i == 1:
                        item['battery_type'] = get_value(p)
                    elif i == 2:
                        item['battery_math'] = get_value(p)
                    elif i == 3:
                        item['charger_type'] = get_value(p)
                    elif i == 4:
                        item['charger_company'] = get_value(p)
                        add_car(item, car_list)
                elif length == 4:
                    if i == 0:
                        item['model'] = get_value(p)
                    elif i == 1:
                        item['battery_type'] = get_value(p)
                    elif i == 2:
                        item['battery_math'] = get_value(p)
                    elif i == 3:
                        item['charger_company'] = get_value(p)
                        add_car(item, car_list)
                elif length == 6:
                    if i == 0:
                        item['producer'] = get_value(p)
                    elif i == 1:
                        item['model'] = get_value(p)
                    elif i == 2:
                        item['battery_type'] = get_value(p)
                    elif i == 3:
                        item['battery_math'] = get_value(p)
                    elif i == 4:
                        item['charger_type'] = get_value(p)
                    elif i == 5:
                        item['charger_company'] = get_value(p)
                        add_car(item, car_list)
    return car_list


def get_one(tr_array, type):
    item = {}
    car_list = []
    for tr in tr_array:
        td_array = tr.find_all('td')
        length = len(td_array)
        for i, td in enumerate(td_array):
            for index, p in enumerate(td.find_all('p')):
                if length == 5:
                    if i == 4:
                        if type == 0:
                            item['model'] = get_value(p)
                        else:
                            item['battery_type'] = get_value(p)
                        add_car(item, car_list)
                    elif i == 1:
                        item['brand'] = get_value(p)
                    elif i == 2:
                        item['producer'] = get_value(p)
                    elif i == 3:
                        if type == 0:
                            item['company'] = get_value(p)
                        else:
                            item['model'] = get_value(p)
                elif length == 3:
                    if i == 2:
                        if type == 0:
                            item['model'] = get_value(p)
                        else:
                            item['battery_type'] = get_value(p)
                        add_car(item, car_list)
                    elif i == 0:
                        item['producer'] = get_value(p)
                    elif i == 1:
                        if type == 0:
                            item['company'] = get_value(p)
                        else:
                            item['model'] = get_value(p)
                elif length == 2:
                    if i == 1:
                        if type == 0:
                            item['model'] = get_value(p)
                        else:
                            item['battery_type'] = get_value(p)
                        add_car(item, car_list)
                    elif i == 0:
                        if type == 0:
                            item['company'] = get_value(p)
                        else:
                            item['model'] = get_value(p)
    return car_list


def add_car(item, car_list):
    model_str = item['model']
    model_list = model_str.split('::')
    for model in model_list:
        car = Car()
        car.source_url = CarHttp.URL
        source = CarHttp.source
        r = re.compile(r'[（](.*)[）]', re.S)
        car.source = re.findall(r, source)[0]
        car.release_time = CarHttp.time
        car.brand = item['brand']
        car.model = model
        car.producer = item['producer']
        car.company = item.get('company')
        car.battery_type = item.get('battery_type')
        car.battery_math = item.get('battery_math')
        car.charger_type = item.get('charger_type')
        car.charger_company = item.get('charger_company')
        car_list.append(car)