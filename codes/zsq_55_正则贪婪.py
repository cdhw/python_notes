#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_55_正则贪婪
# @time: 2018/3/18 15:20
# 正则表达式默认是贪婪匹配，也就是会尽可能地匹配更多的字符
import re

t = '120000'
res = re.match(r'^(\d+?)(0*)$', t)
print(res.groups())
# print(res.group(1))
# print(res.group(2))
sr = "abcdeFGHIJ"
res = re.match(r'^(\w+)([A-Z]*)$', sr)
print(res.groups())