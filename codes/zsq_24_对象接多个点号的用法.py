#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-12 15:26
# @Author  : Henry
# @File    : zsq_24_对象接多个点号的用法.py
# @Software: PyCharm


class Food(object):
    def __init__(self, fruit= "apple"):
        self.fruit = fruit

    def __getattr__(self, item):
        return Food("%s/%s" % (self.fruit, item))

    def __str__(self):
        return self.fruit


f = Food()
print(f.banana.apple)
