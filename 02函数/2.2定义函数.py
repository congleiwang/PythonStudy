#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-15 下午6:13
# @Author  : congl
# @Site    : 
# @File    : 2.2调用函数.py
# @Software: PyCharm

import math


# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。

# 1、空函数

def nop():
    pass


# 2、参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError

# 3、多个返回值

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
t = move(100, 100, 60, math.pi / 6)
print(type(t))
print(t)



