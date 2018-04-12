#!/usr/bin/python
#coding:utf8
class Parent:    #定义父类
    parentAttr = 100

    def __init__(self, user="father"):
        print("调用父类构造函数")
        self.user="father"

    def parentMethod(self):
        print("调用父类方法")

    def setArr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性：", Parent.parentAttr)


class Child(Parent):  # 定义子类
    def __init__(self):
        #Parent.__init__(self)
        super(Child, self).__init__()
        print("调用子类构造方法")

    def childMethod(self):
        print("调用子类方法")

    def getAttr(self):   # 方法重写
        print("我重写了方法")

    def __repr__(self):
        print("适合解释器阅读了吗")

    def __str__(self):
        print("适合人类阅读了吗")

    def __cmp__(self, x):
        print("比较了吗")



c = Child()    # 实例化子类
c.childMethod()
c.parentMethod()
c.setArr(300)
c.getAttr()
# c.user="mother"
c.user = "mom"
print(Child.__bases__)
#repr(c)
str(c)
