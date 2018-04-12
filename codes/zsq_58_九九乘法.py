#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_58_九九乘法
# @time: 2018/3/18 16:40
# 正立的九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        # print(str(i)+"x"+str(j)+"="+str(i*j))
        print(str(i), "x", str(j), "=", str(i*j)," ", end="")
    print("\n")
print(list(range(1,10)))
# 倒立的九九乘法表
for i in list(range(1, 10))[::-1]:
    for j in range(1, i+1):
        print(str(i)+"x"+str(j)+"="+str(i*j), "", end="")
    print("\n")
# 冒泡排序
ls = [1, 3, 5, 7, 9]
for i in range(1,len(ls)):
    for j in range(len(ls)-i):
        k = ls[j+1]
        if ls[j] < ls[j+1]:
            ls[j+1] = ls[j]
            ls[j] = k
print(ls)
