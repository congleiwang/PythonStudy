#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-27下午3:08
# @Author  : congl
# @Site    : 
# @File    : 6.1类和实例
# @Software: PyCharm

# 处理学生成绩
# 面向过程

std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}


def print_score(std):
    print('%s:%s' % (std['name'], std['score']))


# 面向对象
class Student(object):
    # __init__方法绑定类属性,该方法第一个参数一定是类本身
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name, self.score))


bob = Student('Bob', 59)
bob.print_score()
