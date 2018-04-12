#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_65_python特性过滤文件
# @time: 2018/3/19 20:03
# 列出目录下的所有目录
import os
# import hello 之后，需要用hello.xxx的方式访问hello对象中的对象
# 使用hello对象中的任何一个对象都以访问属性的方式
from hello import Apple  # 可以直接使用Apple类
# cont = os.listdir(os.path.abspath(".."))
# cont = os.listdir(os.path.dirname(__file__))
# print(cont)
# print(cont)
# print(os.path.dirname(__file__))  # 获取程序文件所在目录的url
# print(os.path.abspath(".."))  # 当前文件所在目录的绝对路径，路径有两种一种是文件路径、一种是目录路径
print([x for x in os.listdir(os.path.abspath(".")) if os.path.isdir(x)])
# 上面程序'.'和'..'的差距很大，虽然'.'和'..'都能获得目录下的文件夹和文件的名字列表
# 但是只有'.'获取到的当前文件所在目录下的文件夹和文件能够被isdir功能所识别，因为
# 如果我们只给isdir功能传一个文件夹名字或者文件名字的话，他会默认在当前文件所在的目录下寻找
# 也就是相对路径，然后".."获得的是非当前目录下的文件和文件夹名字，所以用相对路径在当前目录下找不到
# 所以'..'返回的是空列表，因为当前找不到这些文件和文件夹，更不要说判断了
# 以上程式如果要用'..'判断上一级目录下的目录有哪些的话，应该如下：
# 获取上一级目录下所有文件或者目录的url
# urls = []
# for x in os.listdir(os.path.abspath("..")):
#     urls.append(os.path.join(os.path.abspath(".."), x))
# print(urls)
# print("上级目录下的目录列表：")
# print([x for x in urls if os.path.isdir(x)])
# url = []
# for i in os.listdir(os.path.abspath("..")):
#     url.append(os.path.join(os.path.abspath(".."), i))
# print([x for x in url if os.path.isdir(x)])
# 声明一个列表对象，用于存放上一级目录下的所有文件url和目录url
urls = []
# 获取urls
# 1、先获取到上一级目录下的所有文件名和目录名的列表
# 2、遍历出每一个文件名或者目录名和上一级目录url拼接
# 3、每一次遍历拼接成功后即获得了文件或者目录的绝对路径，再将其存入urls列表中
# 4、再遍历urls将是目录的对象筛选出来
for i in os.listdir(os.path.abspath("..")):
    urls.append(os.path.join(os.path.abspath(".."), i))
print([x for x in urls if os.path.isdir(x)])
# os.rename("hello.html","hello.py")
# with open("hello.py","w") as a:
#     a.write("import os")
# print(hello.os)
print(Apple)
# print(hello.ap)
# print(hello.a)
# print(hello.gets())