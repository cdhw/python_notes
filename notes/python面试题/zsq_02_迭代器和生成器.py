#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_02_迭代器和生成器
# @time: 2018/4/3 10:37
"""
什么是迭代器？
    迭代器是一个可以被next函数作用并不断返回下一个值的对象
什么是生成器？
    使用了yield的函数被称为生成器，生成器只能用于迭代操作，所以生成器是一种特殊的迭代器


"""
import os
lis = ['1', '3', '4']
bb = iter(lis)  # 创建迭代器实例
# print(next(bb))
# print(next(bb))
# print(next(bb))
# lt = [[1, 2], [3, 4], [5, 6], [7, 8]]
#
#
# def qtlb(name):
#     for a in name:
#         for b in a:
#             yield b
#
#
# def qt():
#     yield [1, 2, 3]
#
#
# for n in qt():  # 迭代生成器迭代出的是生成器yield 后面的值
#     print(n)
# while True:
#     # print(next(bb))
os.rename("zsq_06_python进程中调用shell进程执行命令并获取输出.py", "zsq_06_calloutershell.py")