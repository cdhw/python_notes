#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_15_@staticmethod和@classmethod
# @time: 2018/4/4 10:35


def foo(x):
    print("executing foo(%s)" % (x,))


class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


A.class_foo("jacks")
A.static_foo("static")
a = A()
a.foo("tom")
a.class_foo("jack")
a.static_foo("mary")