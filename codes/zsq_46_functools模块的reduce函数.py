#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_46_functools模块的reduce函数
# @time: 2018/3/17 9:38
from functools import reduce


l1 = [0, 1, 2, 3, 4, 5, 6]


def f4(x, y):
    return x+y


print(reduce(lambda x, y: x+y, l1, 3))
