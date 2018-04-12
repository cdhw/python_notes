#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_13_类的特殊变量__slots__的应用
# @time: 2018/3/10 14:33
from types import MethodType  # 从types包引入MethodType模块(从目录引入文件)


class Student(object):
    pass


#  尝试给对象绑定属性
s = Student()
s.name = 'Michael'  # 动态给对象绑定一个属性
print(s.name)
#  还可以给对象绑定一个方法


def set_age(self, age):  # 定义一个函数作为类的方法
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)
# 但是给一个对象绑定的方法，另一个对象是无法调用的


s2 = Student()  # 创建新的对象
# s2.set_age(25)  # 尝试调用方法
# print(s2.age)
# 若想实现一个所有对象都可以调用的方法，那么可以给类绑定方法


def set_score(self, score):
    self.score = score  # 给对象绑定属性并赋变量值score


Student.set_score = set_score  # 单独看的话，在这里set_score可能是个属性也可能是个方法，但是set_score变量指向的是一个函数主体，
#  所以类添加的是一个方法，方法名为set_score
# s3 = Student()
# s3.set_score(88)
s2.set_score(99)
print(s2.score)
s.set_score(111)
print(s.score)
# 一般说来对象可以在对象内部或者对象外部自由绑定属性并赋值，但是有的时候我们需要限制对象只能绑定给定的属相时，怎么实现呢？
# python允许在定义一个class的时候，定义一个特殊的__slots__变量,来限制该class对象添加的属性


class Teacher(object):
    __slots__ = ("name", "age")  # 用元祖定义允许绑定的属性名称


t = Teacher()
t.name = "zhang"
print(t.name)
t.age = 88
print(t.age)
# t.user = "jack"
# print(t.user)
# tips: __slots__类变量只对当前类的所有对象起作用，对当前类的子类对象是不起作用的






