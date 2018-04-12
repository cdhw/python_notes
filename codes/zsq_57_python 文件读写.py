#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_57_python 文件读写
# @time: 2018/3/18 16:34
"""
python内置了读写文件的程序片段（函数），这些程序片段的调用和C语言是兼容的，
但是无论是python内置程序片段还是C程序片段都是通过调用操作系统接口来读写文件的
具体流程是：我们的应用程序向操作系统请求一个文件对象，然后调用操作系统的相应接口来对这个文件对象进行IO操作
"""

# try:
#     fb = open("zsq_56_正则表达式练习题.py", "r")
#     fb.read()
# finally:
#     if fb:
#         fb.close()
# # print(fb)  # 文件关闭之后，打开的这个文件对象仍然可以调用，只是文件是出于关闭状态不能进行读写
# # try:
# #     print(fb.read())
# # except UnicodeDecodeError as e:
# #     print("错了")
# #     fb.close()
# # finally:
# #     print("查看在文件读失败的情况下是否调用了关闭方法")
# #     print(fb.write("ok"))
# print(fb.read())
# fb.close()
# with open() as xx 语句不用关闭文件，会自动关闭文件
# with open("readfile.html", "r") as a:
#     print(a.read())  # 以字符串的形式读取文件内容至内存
from io import StringIO
# a = open("readfile.html", "r")
# print("读取所有，并返回字符串：")注意：读取整个文件到内存之后，后续再次读取就为空了
# print(a.read())
# print("读取一行并返回字符串：")
# print(a.readline())  # 以上用with语句文件已经自动关闭所以此处无法读取一行
# print("读取所有并按行返回列表：")
# print(a.readlines())
# files = a.readline()
# contents = []
# while files is not "":
#     files = a.readline()
#     contents.append(files)
# print(contents)
# 读取二进制文件
# p = open("zsq.jpg", "rb")
# rb = p.read()
# print("读取到的二进制文件是:")
# print(rb)
# 读取编码不同的文件,下面是要从磁盘读取utf8编码存入的数据，
# 所以要以utf8的方式打开文件对象才能正常显示数据
# fo = open("zsq_56_正则表达式练习题.py", "r", encoding="utf8", errors="ignore")
# print(fo.read())
# fo.close()
"""
写文件：写文件和读文件的流程差不多，唯一不同是open函数的模式参数是"w"或者"wb"表示写入文本数据
和写入二进制数据
"""

# with open("zsq.jpg", "rb") as a:
#     print(a.read())
# 文件的写入
with open("readfile.html", "a+", encoding="utf-8") as a:
    a.write("我爱你")
with open("readfile.html", "r", encoding="utf-8") as a:
        print(a.read())
"""
文件数据存入磁盘的编码和文件数据取出磁盘的解码方式必须一致
"""






