#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: car.py
@time: create by fanxl12 on 2020-05-28
"""
__author__ = 'fanxl12'


class CarIndexModel:
    pass

    def __init__(self):
        self.brand_count = 0
        self.model_count = 0

    def set_brand_count(self, brand_count):
        self.brand_count += brand_count

    def set_model_count(self, count):
        self.model_count = count
