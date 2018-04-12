#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_77_多进程多线程回顾
# @time: 2018/3/26 12:37
from multiprocessing import Process, Pool
import subprocess, time
import threading


def run():
    print("I am running")


'''
if __name__ == "__main__":
    p = Process(target=run)  # 这个子进程只能是当前进程的子进程
    p.start()
    p.join()
'''
"""if __name__ == "__main__":
    p = Pool(3)
    for i in range(8):
        p.apply_async(run)
    p.close()
    p.join()
"""
'''if __name__ == "__main__":
    """p = subprocess.call(["nslookup", "www.baidu.com"])
    print(p)"""
    p = subprocess.Popen(["nslookup"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'www.baidu.com')
    print(output.decode("gbk"))'''
'''
对线程要执行的那段程序上锁，可以让这段程序以单线程模式执行，避免不必要的麻烦
'''

t = threading.Lock()


def run():
    print("hello world!")
    t.acquire()
    print("我开始等待了")
    time.sleep(30)
    print("我等完了30秒")
    t.release()


t1 = threading.Thread(target=run, name="t1")
t2 = threading.Thread(target=run, name="t2")
t1.start()
t2.start()
"""
以上两个线程的执行流程是：python解释器交替执行线程t1、t2中的代码
所以两个线程都会间断地有输出，而不是一个线程一个线程地执行
"""




