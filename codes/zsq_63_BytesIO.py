#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_63_BytesIO
# @time: 2018/3/19 15:57
# BytesIO是一个封装了操作(读和写）内存中二进制数据的方法的对象
from io import BytesIO
b = BytesIO()
b.write("张世强".encode("utf-8"))  # 写入被utf-8编码后的二进制到内存
print(b.getvalue())  # 读取由utf-8编码生成的二进制数据
"""
同StringIO对象一样，可以在生成BytesIO时封装二进制数据到内存
"""
fb = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')  # 封装存入到内存中的二进制数据
# print(fb.getvalue())  # 获取内存中的所有二进制数据
# print(fb.readline())  # 只存了一行，可以读取一行
print(fb.read())  # 可以用read()

