#coding:utf8
member = ["jack", "tom", 'mary']
enmu= enumerate(member) #返回enumerate（枚举）对象，它是一个可迭代对象
print(enmu)
for key,value in enmu:
    print((key,value))