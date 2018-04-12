#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_39_类的属性的获取表达式
# @time: 2018/3/15 16:02


class Animal(dict):
    def __init__(self, **kw):
        super(Animal, self).__init__(**kw)
    # def __init__(self, name="jack"):
    #     self.name = name  # 绑定属性的时候只能用self.name不能用self['name']


a = Animal(user="tom", age=14)
# print(a.user)
# 判断user元素是否是a的属性
print(hasattr(a, "user"))



