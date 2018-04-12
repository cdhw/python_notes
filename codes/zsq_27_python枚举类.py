#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-12 17:51
# @Author  : Henry
# @File    : zsq_27_python枚举类.py
# @Software: PyCharm
# 枚举类基础学习：https://www.cnblogs.com/ucos/p/5896861.html
# 定义枚举类，要导入enum模块
from enum import Enum, unique
import os


class Color(Enum):  # Color类继承了Enum类
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7
# 上面的类，定义了颜色的枚举Color类
# 颜色枚举有7个成员，分别是 Color.red、 Color.orange、 Color.yellow等
# 每一个成员都有它们各自的名称和值，Color.red 成员名是：red 值是：1
# 每个成员的数据类型就是它所属的枚举
# 定义枚举时，成员名称不允许重复
class Fruit(Enum):
    apple = 1
    #apple = 1
# 默认情况下两个不同名称的成员的值是可以相同的，但是具有相同值的两个成员，第二个成员的名称被视作第一个成员的别名
class People(Enum):
    white = 1
    white_alias = 1
# 如果存在相同值的成员，那么通过值获取成员名时，只能获取到第一个成员的名


print(People(1))  # 只能获取到第一个成员的名称 People.white
# 当你想限制定义枚举类时，不能定义相同值的成员，那么可以使用装饰器@unique,即导入unique模块


@unique
class Man(Enum):
    strong = True
    week = False


print(Man(True))
# 通过成员的名称来获取成员
print("————————————————————————————————————————————————————————————")
print(Man["strong"])  # 等价于Man.strong
print(Man.strong)
print("————————————————————————————————————————————————————————————")
print(Man["week"])
# 通过成员的值来获取成员
print(Man(True))
print(Man(True).name)
print(Man(True).value)
print("————————————————————————————————————————————————————————————")
#通过成员来获取它的名称和值
strong_member = Man.strong
print(strong_member.name)
print(strong_member.value)
print("————————————————————————————————————————————————————————————")
# 枚举类的迭代
for i in Color:
    print(i)
print(Color.red)
print(Color(1))
print(Color.red.name)
print(Color.red.value)
print(Color(1).name)
print(Color(1).value)
# 枚举时有重复的成员，循环遍历枚举类时只获取值重复成员的第一个成员
class Co(Enum):
    red = 1
    orange = 2
    yellow = 1

print("————————————————————————————————————————————————————————————")
print("————————————————————————————————————————————————————————————")
for color in Co:
    print(color)

# 如果想把重复值的成员也遍历出来，要用枚举的一个特殊属性__members__

print("————————————————————————————————————————————————————————————")
print("————————————————————————————————————————————————————————————")
print("————————————————————————————————————————————————————————————")
class Cr(Enum):  # 继承了Enum的类就是枚举类
    red = 1
    orange = 2
    yellow = 1


for name, member in Cr.__members__.items():
    print((name, member.name))  # name是成员名、 member是成员
    print((name, member.value))

print("***********************************")
print(Co.red is Co.red)
print(Co.red is not Co.orange)
print(Co.red == Co.red)
print(Co.red == Co.orange)
print(Co.red != Co.orange)
# print(Co.red < Co.orange) # 枚举成员不能进行大小比较
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print(os.listdir("."))
print([i for i in os.listdir(".")])


