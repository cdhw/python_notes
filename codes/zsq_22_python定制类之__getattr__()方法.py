#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-12 11:55
# @Author  : Henry
# @File    : zsq_22_python定制类之__getattr__()方法.py
# @Software: PyCharm

# 当我们用类对象获取一个未绑定属性的值时，程序会报错


def zhang():
    return 999


class Beauty(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __getattr__(self, item):  # item是传入的属性,函数默认都是要返回值的，如果没有写return的话，就会默认返回None
        if item is "tall":
            return 1.74
        elif item is "big":
            return True
        elif item is "hip":
            return lambda: 32
        elif item is "breast":
            return zhang()
        else:
            raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)


b = Beauty("Jane")
print(b.name)
print(b.tall)  # 打印未绑定属性时报错
# 当访问不存在的属性时，可以触发一个方法__getattr__()

print("————————————————————————————————————————————————————————————")
print(b.hip())
print("————————————————————————————————————————————————————————————")
print(b.breast)


