#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-15 下午6:26
# @Author  : congl
# @Site    : 
# @File    : 2.3函数的参数.py
# @Software: PyCharm

# 1、默认参数(定义默认参数要牢记一点：默认参数必须指向不变对象！)
# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


print(enroll('Sarah', 'F'))
print("==============")
print(enroll('Bob', 'M', 7))
print("==============")
print(enroll('Adam', 'M', city='Tianjin'))


# 2、可变参数
# 在函数内部，参数numbers接收到的是一个tuple。
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc())
print(calc(1, 2))
print(calc(1, 2, 3, 4))
# *nums表示把nums这个list的所有元素作为可变参数传进去。
nums = [1, 2, 3]
print(calc(*nums))


# 3、关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
# 把dict转换为关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 4、命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数，命名关键字参数必须传入参数名.
# 例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)


print(person('Jack', 24, city='Beijing', job='Engineer'))
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
# 这意味着可变参数后如果还有参数，那个这个参数一定是命名关键字参数
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
# 命名关键字参数可以有缺省值，从而简化调用：
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


# 5、参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)