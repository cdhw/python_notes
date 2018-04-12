#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_44_python自定义错误抛出
# @time: 2018/3/17 4:49
# 一般的错误抛出都是正常规范的，但是我们也可以指定一种错误并抛出


# class broken(TypeError):
#     pass
#
#
# def foo(n):
#     if n == 0:  # 指定此时为异常
#         raise broken("wrong")
#
#
# foo(0)


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError("invalid value:%s" % s)
    return 10 / n


def bar():
    try:
        foo("0")
    except ValueError as e:
        print("ValueError!")
        raise  # 虽然bar()函数中已经对异常进行了捕捉、一般情况只要捕捉到了异常，except ValueError as e:
    # 下的代码就是对异常的处理，不会再出现红字异常被抛出的情况、但是如果说我们想继续抛出这个异常那么用raise即可
    #  捕获了异常就会将处理代码写出，提示解释器继续干活


bar()


