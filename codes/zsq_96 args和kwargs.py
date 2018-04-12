#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_96 args和kwargs
# @time: 2018/4/3 12:06
# *args和**kwargs, 采用这种参数要注意一点：就是*args要在函数体中将args当做列表看
# 将**kwargs在函数中将kwargs当做字典看


def hit(**kwargs):
    for k in kwargs.items():
        print(k)


hit(name="jack", passowrd=123)


def shout(word="yes"):
    print(word.capitalize())  # capitalize 将一个字符串首字母变大写，其余变小写


shout()

n = 0
while n < 5:
    n = n + 1
    print("a")





