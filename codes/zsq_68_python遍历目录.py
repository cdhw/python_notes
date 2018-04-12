#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_68_python遍历目录
# @time: 2018/3/22 1:33
import os
# 遍历目录第一种：绝对路径


def get_file(cpath):
    for i in os.listdir(cpath):
        j = os.path.join(os.path.dirname(__file__), i)
        if os.path.isdir(j):
            get_file(j)
        else:
            print(j)


cpath = os.path.dirname(__file__)
get_file(cpath)
# 遍历目录第二种：相对路径


def catch_file(content):
    os.chdir(content)
    for i in os.listdir(os.curdir):  # 此处直接调用当前工作目录，不能用content
        if os.path.isdir(i):
            catch_file(i)
            os.chdir(os.pardir)
        else:
            print(os.path.join(os.getcwd(), i))


content = os.path.abspath(".")
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
catch_file(content)
