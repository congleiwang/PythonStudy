#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-27下午4:03
# @Author  : congl
# @Site    : 
# @File    : 6.2访问限制
# @Software: PyCharm

# 在类中定义私有变量
# 实例的变量名以__开头，为私有变量（private），只有内部可以访问，外部不能访问

class Student(object):

    def __init__(self, name, score, gender='male'):
        self.__name = name
        self.__score = score
        self.__gender = gender

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def __set_name__(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


bart = Student('Bart', 18 , 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
