#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_13_ __new__和__init__
# @time: 2018/4/4 8:19
"""
1、由于所有类的基类都是object，而object有一个静态方法__new__，所以每个类在实例化
的时候，其实调用了继承父类的__new__方法，此方法是生成调用者类的实例，生成实例之后
由实例再调用实例方法__init__给自己绑定初始化属性和属性值
"""


class Animal(dict):
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def __new__(cls, *args, **kwargs):
        print("hello")


a = Animal("tom", "jk", 123)
print("Animal的基类有：")
print(Animal.__bases__)
'''以上测试中由于Animal重写了基类object的静态方法__new__导致其在实例化时调用__new__方法没有
生成实例，而是输出"hello", 所以创建Animal的实例失败

'''


def hit():
    print("hit")


Beauty = type("Beauty", (object,), dict(hit=hit, name="tmo", password=1))
# print(type(Beauty))  # 类的类型是type
b = Beauty()
# print(type(b))  # 实例的类型是它的类
print(b.name)
print(type(b))
print(b.__class__)




