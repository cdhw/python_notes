#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_54_正则表达式
# @time: 2018/3/18 9:58
"""
正则表达式是什么？
正则表达式是一种用来匹配字符串的强有力的武器。
正则表达式通过一种描述性的语言来给字符串定义一个规则
然后通过这个规则去匹配字符串，符合的就取、不符合的就pass
举例说：如果我们要判断一个Email是否是合法的，有如下方法：
1、创建一个匹配Email的正则表达式；（创建规则）
2、用该正则表达式去匹配用户的输入来判断是否合法
正则表达式也是用字符串表示的
在正则表达式中，如果直接给出目标字符，就是精确匹配。用\d可以匹配一个数字，\w 可以匹配一个字母或者数字





"""
import re
print(re.match(r'^\d{3}-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}-\d{3,8}$', '010 12345'))


test = "用户输入的字符串"
if re.match(r"正则表达式", test):
    print("ok")
else:
    print("failed")
"""
正则表达式之切分字符串，split函数按照什么字符切，那么这个字符就不存在了
"""
string = "a b    c"
print(string.split(" "))  # split是每隔一个切割字符进行一次切割所以会切割出空格来
# 字符串自带的切割函数识别不了空格
print(re.split(r'\s+','a b c'))  # 表示一个空格或者多个空格都会被切断
print(re.split(r'[\s,]+', 'a,b, c   d'))
print(re.split(r'[\s,;]+', "a, b;; c  d"))
# 分组
res = re.match(r'(\d{3})-(\d{3,8})$', '028-6400211')
print(res)
print(res.group(0))
print(res.group(1))
print(res.group(2))


t = "17:17:17"  # 分、秒都是一样的，小时有三种情况：0和0-9，1和0-9， 2和0-3
res = re.match(r'(0[0-9]|1[0-9]|2[0-3]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])', t)
print(res)
print(res.group(0))
print(res.group(1))
print(res.group(2))
print(res.group(3))
print(res.groups())
# r'[0-9a-zA-Z_]'
sr = "_"
res = re.match(r'[a-z0-9A-Z_]+', sr)
print("sr的匹配结果：")
print(res)
# 用正则匹配2018-03-18
t = "2018-03-18"
t = "1991-02-16"
res = re.match(r'([0-9]+)-(0[1-9]|1[0-2])-(0[0-9]|1[0-9]|2[0-9]|3[0-1])', t)
print("date match:")
print(res)