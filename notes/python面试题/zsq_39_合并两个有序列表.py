#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_39_合并两个有序列表
# @time: 2018/4/12 21:57
# 要求两列表合并后由小到大排序
# 引入一个空列表，一直比较两个列表最小值的大小，小的被弹出
import socket
l1 = [1, 3, 5, 7]
l2 = [6, 4, 3, 2]
l3 = []
while True:
    if l2[-1] > l1[0]:
        l3.append(l1.pop(0))
    else:
        l3.append(l2.pop(-1))
    # if l2[-1] == l1[0]:
    #     l3.append(l2.pop(-1))
    if l2 == [] or l1 == []:
        break


print(l3)
print(socket.gethostname())



