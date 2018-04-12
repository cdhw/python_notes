#coding:utf8
class Student(object):
    def __init__(self, name, score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s:%s' % (self.name,self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()


class Employee:

    '所有员工的基类'
    empCount = 0 #empCount变量是一个类变量，它的值将在这个类的所有实例之间共享，可以在类内部和类外部使用Employee.empcount访问
    def __init__(self, name, salary):#类的构造方法或者初始化方法在实例化类的时候被访问
        self.name = name
        self.salary = salary
        Employee.empCount +=1


    def displayCount(self):#self是类的实例，self在定义类的方法时是必须的，在调用时不用传入相应的参数
        print ("Total Employee: %d" % Employee.empCount)


    def displayEmployee(self):#类的方法和普通函数的区别是：类的方法默认多出了一个self对象参数
        print ("Name:", self.name, ", Salary:", self.salary)


zhangsan = Employee("zhangsan", 18888)
zhangsan.displayEmployee()
zhangsan.displayCount()


class Test:
    "helloworld"
    username="zhangsan"
    def __init__(self, user, id):
        self.user = user
        self.id = id

    def prt(self):
        print(self)
        print(self.__class__)#任何对象共有的属性__class__ self.__class__获取对象对应的类，__name__

    def __del__(self):
        class_name = self.__class__
        print (class_name, "deleted!")

t = Test("zhang", 13)
t.prt()
t.user_name="zhangshiqiang"
# print(t.user_name)
# del t.user_name
print(t.user_name)
# print(hasattr(t, "user_name"))
# print(getattr(t,"user_name"))
delattr(t,"user_name")
# print(t.user_name)
print(t.__module__)
print(t.__dict__)
print(t.__doc__)
del t



