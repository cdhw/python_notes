#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_04_sort()、reverse()
# @time: 2018/4/14 13:11
import random
x = list(range(5))
# random.shuffle(x)
# x1 = str(x)  # 返回一个新的列表字符串，一个全新的对象
# print(id(x1), id(x))
# print(type(x1))
# x.sort()  # 默认按照从小到大的顺序排序
x.sort(key=lambda item: len(str(item)), reverse=True)  # 直接对当前内存地址上的列表排序，并返回当前列表
x.reverse()  # 返回一个已知list的逆向排序list


a = ["apple", "orange", "banban", "pear"]
a.sort()
print(a)  # 按照首字母来
a.sort(key=lambda x1: len(x1))  # reverse为True则从大到小，默认不填，则是小到大
print(a)