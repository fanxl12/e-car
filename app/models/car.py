#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file: car.py
@time: create by fanxl12 on 2020-05-26
"""
__author__ = 'fanxl12'
from app.models.base import Base
from sqlalchemy import Column, Integer, String


class Car(Base):
    id = Column(Integer, primary_key=True)
    brand = Column(String(18), comment='品牌')
    producer = Column(String(32), comment='制造商')
    company = Column(String(32), comment='生产企业')
    model = Column(String(18), comment='型号')
    battery_type = Column(String(8), comment='电池类型')
    battery_math = Column(String(6), comment='电池容量')
    charger_type = Column(String(18), comment='充电器型号')
    charger_company = Column(String(32), comment='充电器生产厂家')
