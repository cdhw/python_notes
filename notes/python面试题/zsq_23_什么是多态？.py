#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_23_什么是多态？
# @time: 2018/4/4 22:07
"""
在类继承当中，同种方法的不同功能实现

"""


class Human:
    def go(self):
        print("Human is going")


h = Human()


class Man(Human):
    def run(self):
        print("Man is running")


class Jack(Man):
    def run(self):
        print("Jack is running")


class Woman(Human):
    def run(self):
        print("Woman is running")


print(Jack.__bases__)


def all_method(ob):
    ob.run()


class Boy:
    def run(self):
        print("boy is running")


all_method(Jack())
all_method(Woman())
# all_method((Human()))
all_method(Boy())
'''
在静态语言中，例如java，all_method方法中的实例必须是Human类的子类，否则
无法调用自己的run方法或者Hunman的run方法，但是由于python是动态语言，所以
即便是一个类他不是Human类的子类，只要它拥有函数all_method中定义的方法，就可以
成功调用all_method方法
'''
