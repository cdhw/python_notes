#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_18_类变量是否是实例的属性
# @time: 2018/4/4 14:31
from types import MethodType

class Animal(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    apple = 4


# a = Animal()
# print(hasattr(a, "apple"))
# print("查看类Animal是否拥有name属性")
# print(Animal.name)
# 实际上a实例只继承了Animal类的一个属性，那就是apple
# 后续的name、sex属性是实例自动给自己绑定的(通过__init__)函数


def hit(self):
    print("hit you ")


Animal.hit = MethodType(hit, Animal)
b = Animal("tom", "jcak")
b.hit()
