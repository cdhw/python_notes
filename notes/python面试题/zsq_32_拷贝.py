#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_32_拷贝
# @time: 2018/4/9 18:09
"""深拷贝：完全拷贝一个对象，相当于新创建一个对象，对象的所有元素指向一个全新的
地址； 浅拷贝：拷贝一个对象的一部分，剩余部分仍然指向原对象，我这里用指针的概念来
加强记忆"""

import copy
ls = [1, 2, 3, 4, [2, 3]]
lss = copy.copy(ls)  # 拷贝了原对象的第一层元素，如果原对象改变第二层元素，它依然会跟随改变
print(lss)
lsss = copy.deepcopy(ls)  # 完全拷贝了原对象，无论原对象怎么变，它不会变
print(lsss)
ls.append(5)
ls[4].append(1)
print(ls)
print(lss)
print(lsss)
