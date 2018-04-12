#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_29_GIL线程锁
# @time: 2018/4/9 8:39
# 一个线程在被python解释器执行之前必须获得GIL锁，且同一时间只有一个线程能够获得GIL锁
# 如果线程处于睡眠状态，GIL锁会自动解除并赋予其他线程
