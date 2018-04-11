#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-15 下午4:53
# @Author  : congl
# @Site    : 
# @File    : 1.3使用list和tuple.py
# @Software: PyCharm

# 1、list 是Python内置列表数据类型，是有序集合

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates[0])
# 使用-1索引代表最后一个元素,-2倒数第二个
print(classmates[-1])
print(classmates[-2])
print(len(classmates), '\n==========')

# （1）、追加元素
classmates.append('Adam')
print(classmates)
# （2）、插入元素，插入到索引1
classmates.insert(1, 'Jack')
print(classmates)
# （3）、删除元素，默认删除最后一个
classmates.pop()
classmates.pop(2)
# （4）、二维数组
L = ['AAA', 11, True]
classmates.insert(3, L)
print(classmates[3][1])

# 2、tuple 元组，tuple一旦初始化就不能修改，这意味着更加安全，尽量使用tuple
# （1）、定义元组
t = ()
t = (1,)
t = (1, 2)
t = (1, 2, ['A', 'B'])
print(t[2][1])
# 修改tuple中的list
t[2][1] = 'C'
print(t[2][1])
