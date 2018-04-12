#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_56_正则表达式练习题
# @time: 2018/3/18 16:07
# 写出Email的正则表达式
import re
email = "zsqq007@163.com"
email ="372055714@qq.com"
email = "someone@gmail.com"
# email = "bill.gates@microsoft.com"
res = re.match(r'^([0-9a-zA-Z_]+)(@[0-9a-zA-Z_]+)(.[a-z]+)$', email)
print(res.groups())
assert res is not None  # 如果断言为真则不会报错

test = "abc1abc"
print(re.match(r'^[a-z]+$', test))

