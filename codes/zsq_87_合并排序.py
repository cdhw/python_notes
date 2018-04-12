#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_87_合并排序
# @time: 2018/3/28 19:09
"""
已知两个相同排序方式的列表，怎样将两个列表合成一个列表，并按照两个列表的排序方式排序

"""
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = []
while True:
    if list1[0] < list2[0]:
        list3.append(list1.pop(0))
    else:
        list3.append(list2.pop(0))
    if list1 == [] or list2 == []:
        break


print(list3)

