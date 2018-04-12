#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_95_enumerate函数
# @time: 2018/4/3 11:34
# enumerate 函数是python的一个内置函数，他可以将可迭代对象转换成带索引的序列，函数返回enumerate对象
# 同时遍历索引和元素
lis = ["apple", "orange", "banana"]
for i in range(len(lis)):
    print((i, lis[i]))
# 以上较复杂，采用enumerate函数来实现
print(list(enumerate(lis)))  # 把列表转换成了带索引的元组列表
quit()
for i in enumerate(lis):
    print(i)
