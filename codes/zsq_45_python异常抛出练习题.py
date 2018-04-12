#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_45_python异常抛出练习题
# @time: 2018/3/17 8:56
from functools import reduce  # functools 包是什么？ 是一个运用于高阶函数的位于lib目录下的一个模块文件
# 从functools模块文件导入（复制粘贴）reduce函数
# from zsq_41_异常捕获 import test
# import zsq_41_异常捕获
print("模块文件的引入测试")
# zsq_41_异常捕获.test()

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXx")


def str2num(s):
    return int(float(s))  # 字符串强制整型转换，对象不能是浮点数字符串，可以先把浮点字符串转化成浮点数再转int


def calc(exp):
    ss = exp.split('+')  # split函数的功能？
    print("ss的值")
    print(ss)
    ns = map(str2num, ss)  # map函数的功能
    print("ns的值")
    print(ns)
    return reduce(lambda acc, x: acc + x, ns)  # reduce函数的功能


def main():
    # r = calc('100+200+345')
    # print("100+200+345=", r)
    r = calc("99 + 88 +7.6")
    print("99 + 88 +7.6 =", r)


main()