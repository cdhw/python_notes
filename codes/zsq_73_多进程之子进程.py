#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_73_多进程之子进程
# @time: 2018/3/25 11:13
"""
子进程往往不是当前程序，而是相对于当前程序之外的程序，创建子进程之后，我们还需要
控制程序的输出和输入，python的subprocess模块的Popen类可以轻松的让我们从当前进程创建出一个
子进程，并且给子进程输入数据或者从子进程获取子进程的输出数据

"""
import subprocess
# print(subprocess.call(["nslookup", "www.cdhwdl.com"]))  # shell参数默认为False，因为命令参数必须以是list
# subprocess.call相当于在命令行下执行了"nslookup www.cdhwdl.com" 命令
# Popen是subprocess模块下面的一个类，这个类绑定的属性非常多
# Popen类有什么功能？  创建新的子进程并和子进程进行数据交互
# subprocess.PIPE 属性的值默认为-1 可以用来初始化stdin stdout stderr 这三个参数的值, 表示需要创建一个新的管道
# subprocess.Popen(args, bufsize=0, executable=None,
#  stdin=None, stdout=None, stderr=None, preexec_fn=None,
#  close_fds=False, shell=False, cwd=None, env=None,
# universal_newlines=False, startupinfo=None, creationflags=0)
# subprocess.PIPE
# 一个可以被用于Popen的stdin 、stdout 和stderr 3个参数的特输值，表示需要创建一个新的管道。
# stderr的值还可以是STDOUT
# 表示子进程的标准错误也输出到标准输出。
# p = subprocess.Popen(["pool.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# output, err = p.communicate(b'www.baidu.com')  # 向开启的子进程中写入数据
# print(output.decode("utf-8"))
# print(p.returncode)
"""
要想对子进程输入数据则必须创建管道也就是stdin为PIPE
同样要想从stdout、stdin获取数据，也必须要创建管道，设置他们的值为PIPE
"""
subprocess.call("nslookup www.baidu.com", shell=True)  # 通过命令执行nslookup程序
# print(res) # 在这里nslookup程序就是当前程序的子程序
# rest = subprocess.call(["nslookup", "www.baidu.com"])
# 此处乱码，是因为shell已经将百度返回的数据解码了，并且和百度编码没有对应
