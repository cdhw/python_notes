#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_41_异常捕获
# @time: 2018/3/16 22:57
# 通常情况下一段程序出现异常时，若是python解释器自己捕获的异常，那么python解释器就是停止工作
# python解释器停止工作，对于我们来说是不利的，所以无论程序中有多少异常
# 我们都不能让python解释器自己去捕捉，而是通过我们的程序自己去捕捉，并记录下异常
# 不让python解释器停止工作，把程序执行完
# python中经典的捕捉异常的语句try...excpet...finally


def test(n):
    try:
        4/n  # "/"是求商、"%"是求余、"//"是求整
    except ZeroDivisionError as e:
        print(e)
    else:
        print("hello")
    finally:
        print("END")
# 当没有捕捉到异常时、else代码块和finally代码块都会被执行


test(1)


try:
    2/1
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("no error!")
finally:
    print("end")
print("______________________________________")

try:
    print("try...")
    r = 10 / int("2")
    print("result:", r)
except ValueError as e:
    print("ValueError:", e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
else:
    print("no error!")
finally:
    print("finally...")
print("END")
print("___________________________________________")
#  当两个except是同类时、先执行前面那个、后面的不会被执行


def boo():
    a = ["a", "b"]
    a = int(a)
    print(a)


def foo():
    boo()


def catch():
    foo()


try:
    catch()
except ValueError as e:
    print("我先")
except UnicodeError as e:
    print("我也知道")
except TypeError as e:
    print(e)
else:
    print("no catch")
finally:
    print("over")


def test():
    print("测试文件是否用作模块，并且文件中的函数调用方式是否是:模块名也就是python程序文件名.函数名")