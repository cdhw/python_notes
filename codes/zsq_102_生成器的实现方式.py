#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_102_生成器的实现方式
# @time: 2018/4/8 16:32
from collections import Iterable
print("方式一：列表生成式[]改()")
print([x * x for x in range(10)])  # 返回一个list,占用内存较大
print((x * x for x in range(10)))  # 返回一个 generator object
# print(type(range(10)))  # 返回一个range object
print("方式二：带yield关键字的函数")


def lb(max):
    a, b, n = 0, 1, 0

    while True:
        if n < max:
            a, b = b, a+b
            yield b
        else:
            break
        n = n + 1


# print(lb(3))  # <generator object lb at 0x00000000006ACFC0>
b = lb(2)  # 必须用变量指向生成器，因为用表达式lb(2)会生成新的生成器
# for i in lb:
#     print(i)
# # while True:
#     print(next(lb))  # 1
# for i in lb(3):  # 生成器可以用于for循环且不会报StopIteration
#     print(i)


def get():
    yield from lb(3)


ge = get()
# print(ge)  # <generator object get at 0x000000000080C0A0>
# 判断ge是不是可迭代对象
print(isinstance(ge, Iterable))
print(next(ge))

