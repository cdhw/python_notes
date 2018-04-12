#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-12 16:18
# @Author  : Henry
# @File    : zsq_25_python定制类之__call__()方法.py
# @Software: PyCharm
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return 1
        # return ("My name is %s" % self.name)


s = Student("henry")
print(s())  #当把对象当做函数调用时就会触发 __call__()方法
# 函数可以直接被调用，对象也可以直接被调用，只要实现了__call__方法
# 判断一个对象是否是Callable对象，可以用callable()函数
print("————————————————————————————————————————————————————————————————————")
print(callable(s))  # callable()函数的参数是一个对象，如果该对象是可调用对象，则返回true，否则报错
