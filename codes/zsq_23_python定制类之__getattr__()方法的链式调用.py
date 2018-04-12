#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-12 15:05
# @Author  : Henry
# @File    : zsq_23_python定制类之__getattr__()方法的链式调用.py
# @Software: PyCharm
# 利用完全动态的__getattr__()方法，可以写出一个链式调用：


class Chain(object):

    def __init__(self, path=""):
        self._path = path

    def __getattr__(self, item):
        return Chain("%s/%s" % (self._path, item))

    def __str__(self):  # 打印封装对象的时候会调用此方法
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)  # 连续返回不同属性值的对象，属性值采用拼接方式，每一次点号后都生成了一个新的数据对象
# 以上程序分两段，第一段是返回对象，第二段是打印对象，打印对象时，触发对象内部的__str__()方法

