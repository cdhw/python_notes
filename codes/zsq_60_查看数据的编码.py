#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_60_查看数据的编码
# @time: 2018/3/19 14:12
"""
当我们从磁盘拿到了一些文本数据，我们想确定这些文本数据是由什么编码存入磁盘的
可以用到chardet这模块的detect方法，detect()方法的参数就是拿到的文本

"""
import chardet
fil = open("zsq_56_正则表达式练习题.py", "rb")
# print("拿到的文本的二进制是：")
# print(fil.read())
print("readfile.html的文本编码是：")  # 要想获取到文本的编码方式，需要以读二进制的方式来获取编码
print(chardet.detect(fil.read()))
