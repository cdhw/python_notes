#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_62_python while True的用法
# @time: 2018/3/19 15:53
"""
'while True:'长循环，也就是会一直循环下去，但是我们可以通过在循环体中添加条件判断
来控制循环的结束
"""
i = 9
while True:
    i -= 1
    if i == -1:
        break
    print(i)
