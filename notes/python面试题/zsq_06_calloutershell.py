#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_06_python进程中调用shell进程执行命令并获取输出
# @time: 2018/4/3 15:09
# 第一种： os.system("cmd")
import os
import subprocess
'''
#  os.system函数只是调用shell执行命令
re = os.system("ls -al")   # 会在shell进程中直接输出命令的返回结果
print(re)  # 执行成功返回0，失败返回1
'''
'''lists = os.popen("ls -al")  # lists是一个打开的文件对象，不会在shell中输出命令的返回结果
而是将结果放入lists中
print(lists.read())  # 读取文件对象中的所有行数据'''
PO = subprocess.Popen("python3", stdout=subprocess.PIPE, shell=False)  # Popen的第一个参数是进程的路径
# 或者进程的shell指令，例如“python” subprocess.Popen就是调用一个外部程序，并通过管道
# 获取外部程序的输出 PO是一个进程对象 PO.stdout 、PO.stderr、 PO.stdin 是打开的文件对象
# print(PO.stdout.read())  # python3进程结束后，这里才能输出
# re = subprocess.call("python", shell=False)  # call函数的第一个参数也是进程的路径或者进程的shell指令
# print("python进程开始了？")
PO.wait()  #  wait方法是等待子进程的完成之后，主进程才往下执行，如果没有，主进程不会等待子进程而
#  直接往下执行
print("hello world")


