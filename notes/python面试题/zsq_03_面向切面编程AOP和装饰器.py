#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_03_面向切面编程AOP和装饰器
# @time: 2018/4/3 14:42
"""
装饰器是一个很著名的设计模式，经常用于有切面需求的场景，例如插入日志，性能测试，事物处理等

"""


def decorate(func):
    print("I am decoration")
    return func


def decorate1(func):
    print("I am decoration1")
    return func


@decorate1
@decorate
def hello():
    print("hello world")


# python中函数都有对象，他们有属性也有方法


