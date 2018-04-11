#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-27下午4:47
# @Author  : congl
# @Site    : 
# @File    : 6.3继承和多态
# @Software: PyCharm

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')