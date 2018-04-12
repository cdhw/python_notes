#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_83_python队列
# @time: 2018/3/27 15:23
import queue
"""
队列的存取方法都有一个block参数：
A、对于put，如果说block为0，则告诉你当前队列满了，并且在未来一段时间
也不可能有空位出来；如果说block为1
"""
q = queue.Queue(maxsize=10)
q.put(10)
print(q.get())