#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_49_断言
# @time: 2018/3/17 11:43


def foo(s):
    n = int(s)
    assert n != 0, "n is zero!"  # 断言n不等于0，要是n等于0，那么就会有异常抛出
    return 10 / n


def hit(who):
    assert who != "tom", "you are so strong!"
    return who


print(hit("jack"))


foo("1")