#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_31_函数式编程
# @time: 2018/4/9 14:48

# filter函数，将可迭代对象中的每个元素放入一个function，然后将function的返回值放入一个
# 序列，最后返回这个序列
from functools import reduce

def no_str(ls):
        if not isinstance(ls, str):
            return ls


print(list(filter(no_str, [1, "a", 2, 3])))


def total(ev):
    ev = ev * ev
    return ev


# map 取出序列的每一个元素进入程序运算，并把每一次的返回值放入一个序列，最后返回序列
m = map(total, [1, 2, 3])
print(list(m))


# reduce函数取出序列的每两个元素参与运算，运算结果再与第三个元素运算，以此类推


def cheng(x, y):
    return x * y


c = reduce(cheng, [1, 2, 3, 4])
print(c)



