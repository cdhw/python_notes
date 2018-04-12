#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_16_args及kwargs
# @time: 2018/3/10 16:40
# python函数可变参数 args和kwagrs
# *args表示任何多个无名参数，是一个元组
# **kwargs表示关键字参数，它是一个dict


def foo(*args, **kwargs):
    print("args=", args)
    print("kwargs=", kwargs)


foo(1, 2, 3)
foo(1, a=1)
foo(1, "b", "c", a=1, b="b")


