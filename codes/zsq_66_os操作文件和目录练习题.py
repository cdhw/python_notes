#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_66_os操作文件和目录练习题
# @time: 2018/3/20 8:11
# 第一题：利用os对象的功能实现 dir -l 命令的输出值
# 分析： dir -l 实现的是什么功能？
# 实现的是获取当前目录下的非隐藏对象
"""
实现思路是：1、先拿到当前目录下的所有对象的列表
2、遍历列表成员，判断其开头是否有"."，没有的就取，反之不取

"""
import os
print([x for x in os.listdir(os.path.abspath(".")) if x[0] == "."])
# 如果说给出的目录不是当前所在目录，也就是说不能利用相对于当前路径来解决了
"""
解决思路：
1、首先要获取到目标目录的url
2、获取到目标目录下的所有对象列表
3、遍历所有对象获取没有"."开头的对象列表
4、遍历非"."开头对象的列表，将遍历出的每一个对象分别和目录url拼接成对象url
并存入列表
"""
# 第二题：获取当前目录下的标志性文件和当前目录下的所有子目录下的标志性文件
"""
分析：在解决问题中，需要涉及哪些流程：
1、首先遍历当前目录下所有对象列表，判断遍历出的对象是目录还是文件，是目录继续遍历目录，是
文件则进行判断
2、以上已经找到了解决问题的循环代码片段，在循环此代码片段的时候只需要只需要传入不同的目录
参数即可
3、定义封装了该代码片段的函数，函数有一个参数，那就是目录的路径
"""


def get_file(curl):
    # print(os.listdir(curl))
    # quit()
    for i in os.listdir(curl):
        j = os.path.join(curl, i)
        # print(j)
        if os.path.isdir(j):
            return get_file(j)
        else:
            print(j)
            # filelist.append(j)


filelist = []
get_file(os.path.abspath("."))
print(filelist)

"""
以上程序中，每一个遍历出的对象实质上只参与同一个程序，那就被判断是否是目录，是继续
参与遍历，不是就被放入列表，程序的执行顺序是从最顶层目录遍历出的每一个对象，开始一个分支
称作顶级对象分支，一个顶级对象分支被完全遍历完之后，开始另一个顶级对象分支的遍历
实质上有很多个for遍历的参与
这个程序模拟的就是我们要查看一目录下的所有文件的流程
"""
'''
print(os.getcwd()+os.sep)  # 获取到当前所在工作目录的路径
print(os.sep)


def scandir(startdir, target):  # 传入两个参数：startdir代表工作目录路径
    # target是寻找目标
    os.chdir(startdir)  # 切换工作目录路径到startdir
    for obj in os.listdir(os.curdir):  # 遍历当前工作目录下的所有对象
        if obj == target:  # 如果遍历对象是目标对象
            print(os.getcwd() + os.sep + obj)  # 打印目标对象的绝对路径
        if os.path.isdir(obj):  # 使用相对于工作目录路径的相对路径判断出不是目标对象，但是是一个目录
            scandir(obj, target)  #
            os.chdir(os.pardir) #!!!


scandir(os.path.abspath("."), "hooks")
'''
os.chdir("D:/codes/test/hello")
print("...........................................")
print(os.curdir)  # 打印当前的工作目录的相对路径
print(os.getcwd())  # 打印当前工作目录的绝对路径
print(os.pardir)



