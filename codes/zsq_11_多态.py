#  coding:utf8
#  新建一个类，这个类可以继承某个现有的类，新的类称为子类，而被继承的类称为基类、父类、或者超类(Base class、Super class)
class Animal(object):
    def run(self):
        print("Animal is running")


class Dog(Animal):
    def run(self):
        print("dog is running")

    def eat(self):
        print("dog is eatting")


class Cat(Animal):
    def run(self):
        print("cat is running")

#  对于Dog来说、Animal是它的父类、对于Animal来说、Dog是它的子类
#  继承的好处？ 最大的好处就是子类获得了父类的全部功能、由于Dog类、Cat类都继承了Animal类，所以即便这两个类什么都没有定义、但是
#  他们已经有了run方法


dog = Dog()
dog.run()
cat = Cat()
cat.run()
#  多态：子类和父类有相同的方法、子类的方法覆盖父类的方法
from tkinter import *

