#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_38_字典类对象的赋值
# @time: 2018/3/15 15:52


class People(dict):
    pass


p = People(user="tom")  # 只要该对象是字典、那么在实例化的时候可以直接给字典绑定无数个属性
print(p)  # 这样会提示p没有user属性
print(getattr(p, "user"))