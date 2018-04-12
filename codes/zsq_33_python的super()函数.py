#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-13 16:47
# @Author  : Henry
# @File    : zsq_33_python的super()函数.py
# @Software: PyCharm
# super函数用于调用父类或者说超类的一个方法
# super是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没有问题，但是如果使用多继承，会
# 涉及到查找顺序(MRO)、重复调用(钻石继承)等种种问题
# MRO就是类的方法解析顺序表，其实也就是继承父类方法时的顺序表
# 以下是super()方法的语法
# super(class[,object-or-type]) class是类名、object-or-type对象、一般是self
# super()函数在python2和python3的区别是python3用super().xxx来代替了python2的super(class, self).xxx
class A:
    def add(self, x):
        print("you need add "+x)


class B(A):
    def add(self, x):
          super().add(x)
         # super(B,self).add(x) 等效于python3的super().add(x)


b = B()
b.add("hello")