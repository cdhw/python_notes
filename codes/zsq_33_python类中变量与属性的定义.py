#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_33_python类中变量与属性的定义
# @time: 2018/3/14 8:54


class Animal(object):
    duck = 1
    elephant = 2
    cat = 3

    def __init__(self, act):
        self.act = act


a = Animal("run")
a.duck = 888
print(a.duck)
print(a.act)
print(a.elephant)






