#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_70_json对象
# @time: 2018/3/23 15:51
import json, os
"""
python中的json对象就是JavaScript中的对象
我们要想在不同的语言程序间传递数据，那么我们序列化出来的数据应该有一个统一的标准
通常我们使用的统一标准序列化数据是XML和JSON，json有诸多优点：
1、本身就是一个字符串，方便各种编程语言读取、方便磁盘存储、方便传输
2、方便，json可以直接在web页面中被读取
3、是标准的数据格式
4 json存储默认用的编码是utf8
"""
#  下面尝试把python字典转换成json格式
dic = dict(name="张三", age=20, score=88)  # 在这里是实例化了一个字典对象,并给其添加了3个元素
# 实例化dict时传递的3个参数并非绑定的dic的属性，而是dic的3个元素，所有不能用dic点号访问
# 现在尝试把dic字典转换成json
dj = json.dumps(dic, ensure_ascii=False)  # json序列化时默认输出的中文是ascii的编码，不是真正的中文
print("添加ensure_ascii参数后，dic字典转换成json之后是："+dj)
# 同pickle对象一样，仍然可以把字典对象转换成json对象后直接写进文件，
# 这种方法看不到转换出来的json，写进文件后，会覆盖文件之前的内容，可以用a追加的方式
with open("hello.txt", "w", encoding="utf-8") as a:  # 用utf8编码写数据进磁盘
    json.dump(dic, a)
#  把json从文件中加载出来并反序列化得到字典
with open("hello.txt", "r", encoding="utf-8") as a:  # 用utf8解码磁盘数据
    print(json.load(a))  # 将json从文本反序列化得到python字典
# 把json直接反序列化为字典
print(json.loads(dj))
"""
python 字典可以直接序列化成json，但是我们通常用类来表示对象
所以类对象要能序列化成json才行


"""


class Beauty(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


b = Beauty("张三", 150)


def beauty_dict(obj):  # 对象变字典
    return obj.__dict__


print("将类对象序列化获得json的结果：")
oj = json.dumps(b, default=beauty_dict, )
print(oj)  # 一般情况下，类对象是不能转json的，需要先把类对象变字典对象
# 再看怎样由json反序列化获得类对象


def dict_beauty(di):  # 字典变对象
    return Beauty(di['name'], di['score'])


print("将json反序列化获得类对象的结果：")
jo = json.loads(oj, object_hook=dict_beauty)
print(jo)
#  楼上实现的只是将类对象封装的数据序列化存到了磁盘，然后又从磁盘取出绑定给了类对象
print("查看当前进程的父进程")
print("Process %s start ..." % os.getpid())


