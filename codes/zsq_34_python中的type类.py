#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_34_python中的type类
# @time: 2018/3/14 9:06


class God:
    pass


g = God()
# type(g)
print(type(g))
print(type(1))  # 1是int的对象
print(id(g))  # id函数获取对象在内存中的位置
print(type(object))  # object是type类型，所以object是type的实例
print(object.__class__)   # __class__属性可以获取实例或者类型的名字,object实际上是一个实例化的对象、而type就是一个类型
print(type.__class__)  # 显示type就是一个类型
print("+++++++++++++++++++++++++")

