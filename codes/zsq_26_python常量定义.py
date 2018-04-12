#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-12 16:45
# @Author  : Henry
# @File    : zsq_26_python常量定义.py
# @Software: PyCharm
# 定义常量的一个办法是用大写字母通过整数来定义，例如定义月份：
from enum import Enum
JAN = 1
FEB = 2
MAR = 3
NOV = 11
DEC = 12
# 以上定义常量的方式的好处是简单，缺点是数据类型是int、并且仍然是变量
# 更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一对象。
# python提供了Enum类来实现这个功能
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name, member in Month.__members__.items():
#     print(name, "=>", member, ",", member.value)
class Beauty(object):
    def __init__(self):
        self.name="zhang"
        self.sex="男"
    name = "zhang"
    sex = "男"


print(Beauty.name)
print(Beauty.sex)