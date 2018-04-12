#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_28_怎样删除列表中的重复元素？
# @time: 2018/4/8 22:15
import copy
a = [1, 1, 2, 2, 3, 3, 9, 9, 8, 8]
# print(range(len(a)))
'''di = {}
for i in range(len(a)):

        di[a[i]] = i


for j in di:
    print(j)'''
le = len(a)
b = copy.deepcopy(a)
for i in range(le):
    for j in range(le):
        if i != j and a[i] == a[j]:
            a[j] = str(a[j])


print(b)
