#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_47_python map函数
# @time: 2018/3/17 10:08


def hit(n):
    return n**2


l = [1, 2, 3, 4, 5, 6]


print(list(map(hit, l)))