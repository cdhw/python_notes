#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_15_装饰器
# @time: 2018/3/10 16:16

# 函数也是对象，并且函数对象可以被赋值给变量，所以，通过变量也能调用该函数

# @log
# def now():
#     print("2018-03-10")
#
#
# f = now
# f()


# 函数对象有一个__name__属性， 可以拿到函数的名字
# print(now.__name__)


def show():
    print("hands up")


s = show
s()
print(show.__name__)  # 函数对象的__name__ 属性获取到了函数的名字


# 如果我们想增加函数now()的功能，但是又不想更改now()函数的定义，而是在now()函数在被调用执行的过程中又增加其他的功能，这种
# 在代码运行期间动态增加功能的方式，称之为装饰器(Decorator)
# 本质上装饰器就是一个能够返回函数的高阶函数
# 以下举例 定义一个能打印日志的Decorator（装饰器）


def log(func):
    def wraper(*args, **kwargs):
        print("call %s:" % func.__name__)
        return func(*args, **kwargs)
    return wraper


@log
def now():
    print("2018-03-10")


now()
