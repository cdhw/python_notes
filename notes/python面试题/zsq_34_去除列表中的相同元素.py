#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_34_去除列表中的相同元素
# @time: 2018/4/9 23:40
print("方法一：采用集合转换")
'''ls = [1, 1, 2, 2]
s = set(ls)  # 获取集合，集合没有重复元素
print(type(s)) # 打印集合类型
lis = list(s)  # 将集合转换成列表
print(lis)'''
print("方法二：采用字典转换，未保存原列表顺序")
'''l1 = ['b', 'c', 'd', 'b', 'c', 'a','a']
print({}.fromkeys(l1))  # 将列表的元素作为键，值为None放入一个字典中
print({}.fromkeys(l1).keys())  # 获取None值字典的所有键并放入一个dict_keys对象中
l2 = {}.fromkeys(l1).keys()
print(list(l2))  # 将dict_keys字典转换成列表'''
print("方法三：采用字典转换，且保存原列表顺序")
l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
print(l1.index())
l2 = list(set(l1))
print(l2)  # d b a c 顺序已打乱
l2.sort(key=l1.index)  # 按照l1的排序
print(l2)

