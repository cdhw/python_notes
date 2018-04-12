#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_19_python 类的__call__方法
# @time: 2018/4/4 16:22


class X(object):
    def __init__(self, a, b, range):
        self.a = a
        self.b = b
        self.range = range

    def __call__(self, a, b):
        self.a = a
        self.b = b
        print('__call__ with （{}, {}）'.format(self.a, self.b))

    def __del__(self):
          print("over")


x = X(1, 4, 5)
x(2, 3)  # 若要把实例当函数用，实例必须拥有__call__方法