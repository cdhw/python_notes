#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:zhangshiqiang
# @contact: zsqq007@163.com
# @file: zsq_18_多重继承
# @time: 2018/3/11 17:42


class Animal(object):
    pass


# 大类
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


# 如果要给以上动物加上跑和飞的功能，只需要定义好Runnable和Flyable的类


class RunnableMixIn(object):
    def run(self):
        print("running")


class FlyableMixIn(object):
    def fly(self):
        print("Flying")


# 对于需要Running功能的动物，就多继承一个Runnable，例如Dog：
# class Dog(Mammal, Runnable): # 这里Mammal和Runnable没有直接联系，只有间接联系，都继承自object
    # pass


# 对于需要Flying功能动物，就多继承一个Flyable，例如Bat：
class Bat(Mammal, FlyableMixIn):
    pass


# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如Ostrich继承自Bird。但是该类需要附加额外的功能，通过多重继承就可以实现
# 例如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种为附加功能而产生的继承设计称之为MixIn
# 除了顶级父类，其他的为增加功能而继承的类我们通常用MixIn作后缀
class Dog(Mammal, RunnableMixIn, FlyableMixIn):
    pass


# python自带的很多库也使用MixIn，例如，Python自带了TCPServer和UDPserver这两类网络服务，而要同时服务多个用户就必须
# 多进程或者多线程模型， 这两种模型由ForkingMixIn和ThreadingMixIn提供，通过组合，我们就可以创造合适的服务来
# 比如，编写一个多进程模式的TCP服务，定义如下：
class TCPServer:
    pass


class ForkingMixIn:
    pass


class MyTCPServer(TCPServer, ForkingMixIn):
    pass


# 编写一个多线程模式的UDP服务，定义如下：
class UDPServer:
    pass

class ThreadingMixIn:
    pass


class MyUDPServer(UDPServer, ThreadingMixIn):
    pass


# 协程模型
class CoroutineMixIn:
    pass


class MyTCPServer(TCPServer, CoroutineMixIn):
    pass

# 总之，针对你的类，你需要什么要的额外功能就继承相应的类即可
# 可以通过创建子类，子类继承各种功能的类，从而实现各种类的功能组合
# 就好一个人拜了多个师傅，师傅们的技能可以在徒弟一个人身上综合表现出来
# tips：python支持多重继承 但java不支持








