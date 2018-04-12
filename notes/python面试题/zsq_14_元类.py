#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_14_元类
# @time: 2018/4/4 9:47
"""什么是元类？
元类就是控制其他类的定义的类
"""


class AppleMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        attrs['add'] = lambda self, x: self.append(x)
        attrs['username'] = 'jack'
        print("mcs是")
        print(type(mcs))
        return type.__new__(mcs, name, bases, attrs)


# Apple = type("Apple", (dict,), dict(metaclass=AppleMetaclass))
class Apple(list, metaclass=AppleMetaclass):
    pass


a = Apple()
# a.username = "hello"
print(a.username)  # 引用的类变量,类变量是所有实例都能访问到的一个变量
a.username = "jack"  # 非类属性了，绑定成了a的独有属性
b = Apple()
print(a.username)
print(b.username)



