#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_python字典元素变属性
# @time: 2018/3/15 18:10
# 因为对象在访问未知属性时会触发__getattr__方法来试图获取未知属性值的方法，如果获取到了未知属性的值
# 那么就相当于对象绑定了此未知属性，关键一点__getattr__返回的一定是未知属性的值


class Beauty(dict):
    def __getattr__(self, item):  # 此方法实现了字典元素变方法
        print("find me")
        return self[item]


b = Beauty(username="jack", password=123, id=456)  # 此处相当于给b字典添加了三个元素
# print(b.username)  # 触发了__getattr__并绑定元素为属性
# print(hasattr(b, "username"))
# print(hasattr(b, "password"))  # hasattr在尝试判断password是否是属性时也会触发__getattr__方法
print(Beauty.__dict__)

