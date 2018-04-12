# !usr/bin/python
# coding:utf8


class Animal:
    def __init__(self,tiger=18,bird=19):
        self.tiger = tiger
        self.bird = bird
        self._password = 123

    def __str__(self):
        return "Animal (%d,%d)" % (self.tiger, self.bird)

    def __add__(self, other):
        return Animal(self.tiger+other.tiger, self.bird+other.bird)


v1 = Animal(4,6)
v2 = Animal(4,8)
# print(v1.__password)
print(v1+v2)

class Cat(Animal):
    def __init__(self, cat=19):
        self.__cat = cat
        Animal.__init__(self)

    def get_password(self):
       print(self._password)

    def get_cat(self):
        print(self.__cat)# 私有的属性只能在类内部直接获取，然后通过函数在类外间接获取


c = Cat()
c.get_password()
c.get_cat()



