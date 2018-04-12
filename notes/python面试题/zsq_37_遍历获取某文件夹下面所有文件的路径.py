#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_37_遍历获取某文件夹下面所有文件的路径
# @time: 2018/4/12 8:50
import os
# 通过绝对路径的方式获取文件夹下所有文件的绝对路径
print("--------------------------------------------------------------------")


def get_all_files_url(content_url):
    # 根据给出的文件夹对象的绝对路径获取当前文件夹下的所有对象名称（包括文件夹和文件）
    all_object = os.listdir(content_url)
    for ob in all_object:
        ob = os.path.join(content_url, ob)
        if not os.path.isfile(ob):
            get_all_files_url(ob)
        else:
            print(ob)


# print(os.path.abspath('.'))  # 获取当前文件所在目录的绝对路径
# print(os.path.dirname(__file__))
# print(os.path.dirname())  # 获得父父级目录绝对路径

# get_all_files_url(os.path.abspath('.'))
# get_all_files_url(os.path.dirname(__file__))
print("--------------------------------------------------------------------")


# 通过相对路径获取指定url目录下所有文件的url


def get_all_files_url_by_short_url(content_url):
    # 将工作目录切换到目标文件夹

    os.chdir(content_url)
    all_ob = os.listdir(content_url)
    for x in all_ob:
        if not os.path.isfile(x):
            x = os.path.join(content_url, x)
            get_all_files_url_by_short_url(x)
            os.chdir(os.pardir)
        else:
            print(os.path.join(content_url, x))


get_all_files_url_by_short_url(os.path.dirname(os.path.abspath(".")))








