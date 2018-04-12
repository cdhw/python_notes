#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_64_用os对象和os.path对象操作文件和目录
# @time: 2018/3/19 16:24
import os, shutil
print("操作系统的类型是："+os.name)  # 输出“nt”表示windows操作系统
# print("操作系统的详细信息"+os.uname())  # windows操作系统没有提供uname函数对应的接口
"""
环境变量
"""
# 获取操作系统中定义的所有环境变量
print("操作系统中的环境变量有：")
print(os.environ)
print("操作系统的path环境变量有："+os.environ['path'])

# 查看当前程序文件所在目录的绝对路径
print("当前程序文件所在目录的绝对路径是："+os.path.abspath("."))
# 新创建目录是有讲究的，因为不同的操作系统路径分割符是不一样的，
# 所以我们不能通过字符串拼接的方式来拼接路径，然后通过拼接的路径来创建目录
# 在创建目录之前，我们需要通过程序生成创建目录的路径，
# 通过程序生成创建目录的路径就避免了操作系统的差异带来的路径分隔符的错误
# filemake = os.path.join(os.path.abspath("."), "test")  # 先拼接处需要创建出的目录的路径
# os.mkdir(filemake) # 创建目标目录
fob = os.path.join(os.path.abspath(".."), "test")  # 先创建出目标目录的路径
# os.mkdir(fob)  # 创建目标目录
"""
以上是拼接目标目录的路径，提醒不要用字符串拼接的方式，同样拆分路径时，也不要用拆分
字符串的方式去拆分路径
"""
print("将一个文件的url从文件名处分割")
sp = os.path.split(__file__)  # 目录和文件一分为二、、os.path对象的split函数的功能是将路径的最后一个单元
# (最后一个单元可能是文件也可能是目录)拆分出来
# 整个路径一分为二，返回由这两部分组成的元组
print(sp)
print("将一个目录url从最后一个目录处分割")
d = os.path.split(os.path.abspath("."))
print(d)  # 目录和目录一分为二

print("打印当前程序文件名："+sp[1])
ext = os.path.splitext(__file__)  # 目录带文件名和文件后缀一分为二、、此功能是以最后一个文件的后缀为单位拆分整个路径，获得两部分
# 组成的元组
print("将一个文件的url从文件的.位置分割")
print(ext)
##########################
# 文件重命名
print("文件重命名")
if os.path.exists("zsq.jpg"):
    os.remove("zsq.jpg")
# os.rename("zsq.jpg", "zq.jpg")
print("目录重命名")
# os.rename("test1", "test")
print("删掉文件")
# os.remove("zq.jpg")
print("删掉目录")
# try:
#     os.remove("test")
# except PermissionError as e:
#     print("删除不了")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
# print(os.listdir("test"))
# if os.path.exists("test") and os.listdir("test") == []:
#     print("删除空目录")
#     os.rmdir("test")
# quit()
print("创建新目录")
# if not os.path.exists("test"):
#     os.mkdir(os.path.join(os.path.abspath("."), "test"))
print("删除非空目录,我们用shutil对象")
if os.path.exists("test") and os.listdir("test") == []:
    print("删除空目录")
    shutil.rmtree("test")   # shutil对象的rmtree功能不但可以删除空目录还可以删除非空目录
    # os.rmdir("test")
elif os.path.exists("test") and os.listdir("test") != []:
    print("删除非空目录")
    shutil.rmtree("test")
else:
    print("不存在")
"""
shutil对象可以看做是os对象的补充
"""
#  shutil 对象的复制文件功能 copyfile()
print("shutil的复制功能")
shutil.copyfile("readfile.html", "index.html")  # 将readfile.html中的内容复制到另外一个文件
# 若文件不存在，创建文件并复制内容进入文件，上面的index.html是不存在
# 复制文件到存在的文件
shutil.copyfile("readfile.html", "test1.py")  # 若复制文件已经存在，那么被复制的文件内容
# 会覆盖复制文件原内容
shutil.copyfile("readfile.html", "hello.html")




