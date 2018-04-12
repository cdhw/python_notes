#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_69_序列化
# @time: 2018/3/22 9:31
"""
一般情况下，对象都是python解释器工作的时候动态加载到内存中去的，对象的表达式存在于文本，而
实现的对象是存在内存中的。如果我们不把对象存储到磁盘，那么对象的状态就是文本记录的状态


"""
import pickle


c = dict(username="tom", password="abc", sex="boy")  # 实例化一个字典对象
cps = pickle.dumps(c)  # 序列化成字节码
print(cps)
cp = pickle.dump(c, open("index.html", 'wb'))
uncps = pickle.load(open("index.html", 'rb'))  # 将文件中序列化了的部分反序列化成字典对象
print("从文件中反序列化字节码得到python原字典：")
print(uncps)
uncp = pickle.loads(cps)  # 将现有的字节码反序列化成字典对象
print("直接反序列化字节码得到：")
print(uncp)
"""
一般我们用pickle对象保存一些不重要的数据，因为时候可能反序列化失败
"""









