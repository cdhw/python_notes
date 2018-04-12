#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_67_遍历目录下所有目录获取目标文件
# @time: 2018/3/20 21:34
import os
"""
有两种方式：第一种是通过绝对路径，此方式比较简单也是最直接的方式
第二种是通过相对路径的方式，此方式相对复杂，要绕一些
"""
# 介绍第一种：绝对路径
"""
思路：
1、已知目录A的url
2、通过os的listdir功能获取目录A下的所有文件名、目录名列表
3、遍历列表
4、根据已知A目录url拼接出每一个对象的绝对url
5、用os对象中的path对象的isdir功能判断对象是目录还是文件
6、是目录的对象继续重复1到5步
7、不是目录的（也就是文件）对象直接存入列表
8、将1到7步定义成一个函数对象
"""


def get_file(path):
    for x in os.listdir(path):
        y = os.path.join(path, x)
        if os.path.isdir(y):
            get_file(y)
        else:
            print(y)


print("绝对路径：XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx")
path = os.path.dirname(__file__)
print(path)
get_file(path)


# 介绍第二种:相对路径
"""
使用相对路径，需要用到os对象的几个功能和属性
os.curdir:获取当前工作目录的相对路径"."
os.getcwd():获取当前工作目录的绝对路径
os.pardir:获取当前工作目录的上一级目录的相对路径".."
os.chdir()切换工作路径
思路：
1、已知目录A的绝对url
2、将工作目录切换到A
3、通过os的listdir功能获取目录A下的所有文件名、目录名列表
4、遍历列表
5、判断遍历出的每一个对象是否是目录
6、是目录，将工作目录切换到遍历对象所在目录，在重复1到5步，但是当前目录重复完了之后
要记得将工作目录切换至上一级目录，已方便进行父级目录下的其他目录的遍历
7、不是目录，打印出来
8、将1到7步封装成函数对象
"""
print("相对路径：AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")


def print_file(paths):
    os.chdir(paths)
    for i in os.listdir(os.curdir):
        if os.path.isdir(i):
            print_file(i)
            os.chdir(os.pardir)
        else:
            print(i)


url = os.path.dirname(__file__)
print_file(url)

