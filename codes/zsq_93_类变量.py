#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_93_类变量
# @time: 2018/4/3 0:07


class Animal(object):
    name = []


a = Animal()
b = Animal()
a.name = "cat"  # 引用的类变量被改变了（列表变字符串），变成了实例属性
a.name.append("cat")  # 引用的类变量，没有改变类变量（还是列表）
print(a.name)
print(b.name)