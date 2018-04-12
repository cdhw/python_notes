#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_61_StringIO对象
# @time: 2018/3/19 15:42
# StringIO对象是操作内存中字符串的一个对象
# StringIO对象封装了操作内存中字符串的功能和数据
from io import StringIO
f = StringIO()
f.write("hello,zsq!")
print("试试看可以不可以用read()")
print(f.read())  # 不可以
print("XXXXXXXXXXXXXXXXX")
print(f.getvalue())
# 和上面等同的方法是在创建StringIO对象的时候给其封装字符串属性，相当于给
# 内存中写入字符串数据
ff = StringIO("hello,world,\nhow are you?,\nI miss you!")
print("打印出StringIO对象封装的写入内存中的字符串")
print(ff.getvalue())  # 获取写入的所有字符串
while True:  # while True 表示一直循环，但是我们可以在循环体中写停止循环的条件
    s = ff.readline()
    if s == "":
        break
    print(s.strip())
