#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-13 15:24
# @Author  : Henry
# @File    : zsq_32_python metaclass应用于ORM.py
# @Software: PyCharm

# 在ORM（对象-关系映射)中，所有的类都只能动态定义（也就是每一次python解释器执行该类
# 的定义代码时都有可能生成不一样的类）
# 以下尝试编写ORM框架
# 编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用
# 这个ORM框架，想定义一个User类来操作对应的数据库表（通过user类来操作user表）
# 那么代码可以这样写
# 接下来 编写控制Model类生成的ModelMetaclass类
# 书写代码时，类的定义顺序很重要、一般会根据类的使用先后顺序定义类


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.colum_type = column_type

    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.name)  # __class__是类的特有属性 用于获取类或者对象的类型


# f = Field("jack", "str")
# print(Field.__name__)  # __name__是类独有的属性，只有类才能调用此属性，对象不能调用，获取的是类的名字
# 以上Field对象只能封装一个字段的名称和字段的数据类型
# 实际上一个表中会有很多个字段名和不同的字段数据类型


class StringField(Field):
    def __init__(self, name):
        super().__init__(name, "varchar(100)")


class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, "bigint")

# 以上画红线的Model类,IntegerField()、 StringField()函数是由框架ORM提供的
# 方法save()是由metaclass类自动完成的、metaclass类的编写非常复杂、但是ORM的使用者操作却很方便
# 现在按照上面的接口来实现ORM框架
# 首先定义Field类，这个类的作用是保存数据库表的字段名和字段类型


class ModelMetaclass(type):
    def __new__(mcs, name, bases, attrs):  # __new__方法就是ModelMetaclass类控制Model类的方法
        if name == 'Model':  # 判断如果说name类名是Model的话
            return type.__new__(mcs, name, bases, attrs)
            # print("打印此处返回的类型：")
            # mo = type.__new__(mcs, name, bases, attrs)  # 此处返回的是Model类型的实例，也就是ModelMetaclass作用的那个类的实例
            # print("打印出Model类型实例的所有属性和方法：")
            # print(dir(mo))
            # print(mo.__dict__)
            # print(type.__new__(mcs, name, bases, attrs))
        print('Found model: %s' % name)  # 打印ModelMetaclass类作用的那个类的名字
        mappings = dict()  # 定义一个空字典
        # print("打印mappings的类型：")
        # print(type(mappings))  # 字典类型，说明它是字典的实例化对象
        # print("打印出attrs的值：")
        # attrs是一个字典
        # {'__qualname__': 'User', 'name': <__main__.StringField object at 0x00000000006EBDA0>,
        #  '__module__': '__main__', 'email': <__main__.StringField object at 0x00000000006EBDD8>,
        #  'password': <__main__.StringField object at 0x00000000006EBE10>,
        #  'id': <__main__.IntegerField object at 0x00000000006EBD68>
        # }
        # 字典的元素包含了最后一个继承了Model类的User类的所有属性和属性值
        # print(attrs)
        print("打印出attrs.items()的值：")
        print(attrs.items())  # 元组列表
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        print("打印此时的attrs：")
        print(attrs)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(mcs, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        print("使用了Model的构造函数")
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        print("打印fields：")
        print(fields)
        print("打印args:")
        print(args)
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    id = IntegerField("id")
    name = StringField("username")
    email = StringField("email")
    password = StringField("password")


u = User()  # User类的属性初始已经给了，给的是封装了字段名和字段类型的对象
# print("查看u是否有id属性")
# print(u.id)  # 结果是：没有
print("下面查看u的类型")
print(type(u))  # 他是User的实例化类
# 查看实例u的所有属性和方法
print("打印被ModelMetaclass作用后生成的User类的属性和方法：")
print(dir(u))
# 创建一个对象
k = User(id=12345, name="Michael", email="test@orm.org", password="my-pwd", user="zhang", num =1)
print("打印字典k")
print(k)  # k是一个字典
print("判断字典k的元素是否是他的属性")
print(hasattr(k, "name"))
print("打印此时的User实例的属性和方法：")
print(dir(k))
# 查看此时k的__mappings__属性
print("打印此时k的__mappings__属性：")
print(k.__mappings__['email'].colum_type)
# 保存到数据库
k.save()
print(k.user)

print("dict 的类型是：")
print(type(dict))
print("type的类型是")
print(type(type))


print("下面测试两个继承关系的类的类型分别是什么：")


class Father:
    pass


class Son(Father):
    pass


print("查看Father类的类型")
print(type(Father))  # 是type类型
print("查看Son类的类型")
print(type(Son))  # 是type类型，所有的类都是继承自object类，所以object是所有类的超类
#  但是即便是顶级超类也是type类的实例，
print(type(object))  # 类型的最高级别是type、 超类的最高级别是object
ss = Son()
print(type(ss))
print("object 的超类是：")
print(type.__bases__)   # type的超类是object
print(object.__bases__)  # object的超类为空，说明object是最顶级超类











