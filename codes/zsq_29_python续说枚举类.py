#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-12 22:03
# @Author  : Henry
# @File    : zsq_29_python续说枚举类.py
# @Software: PyCharm
# 可以通过大写字母、值为整数来定义常量，例如：
from enum import Enum


JAN = 1
FEB = 2
MAR = 3
NOV = 11
DEC = 12
# 以上定义的好处是简单、缺点是类型是int, 并且仍然是变量
# python的Enum类可以将以上枚举类型定义成一个class类型，枚举类型中的每一个常量都是class类型的实例化对象
M = Enum("Month", ("Jan", "Feb", "Mar", "Nov", "Dec"))  # 获取到了名为Month的枚举类,默认给枚举成员赋值1，2..
print(M.Jan)  # 枚举成员
print(M.Jan.name)
print(M.Jan.value)
print(M.Feb.name)
print(M.Feb.value)
# 枚举类可以避免类中属性使用字符串
class Mem(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


class Sex(Enum):
    male = 0
    female = 1


print("________________________")
m = Mem("Mary", Sex.female.value)
print(m.sex)

