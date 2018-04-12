#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_82_分布式进程
# @time: 2018/3/27 12:08
"""
在Thread和Process中，应该优选Process，因为Process更为稳定，并且Process
可以分布到多台机器上，而Thread只能部署到同一台机器的不同cpu上。
python的multiprocessing 模块不但支持多进程，其中的managers子模块还可以
把进程分布到多台机器上去
一个服务进程可以作为调度者，依靠网络通信，将任务分配到其他多个进程中去
通过managers模块，我们可以不必了解网络通信的细节，就可以很容易地编写
分布式多进程程序
"""
import random, time, queue
from multiprocessing.managers import BaseManager
# 发送任务的队列：
task_queue = queue.Queue()  # 实例化队列类获取的队列对象
# 接收结果的队列：
result_queue = queue.Queue()


# BaseManager 是进程管理模块managers下的一个类
# 定义一个队列管理类QueueManager，继承BaseManager类


class QueueManager(BaseManager):
    pass


# 把两个Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000， 设置验证码‘abc’
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue：
manager.start()
# 获得通过网络访问的Queue对象：
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去
for i in range(10):
    n = random.randint(0, 10000)
    print("Put task %d.." % n)
    task.put(n)
# 从result队列读取结果
print("Try get results...")
for i in range(10):
    r = result.get(timeout=10)
    print("Result:%s" % r)
# 关闭
manager.shutdown()
print("master exit.")
