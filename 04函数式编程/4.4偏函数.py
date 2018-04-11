#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-27上午9:00
# @Author  : congl
# @Site    : 
# @File    : 4.4偏函数
# @Software: PyCharm

import functools

# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单。

# kw = { 'base': 2 }
# int('1010', **kw)

int2 = functools.partial(int, base=2)
print(int2('1010'))

# args = (10, 5, 6, 7)
# max(*args)
max2 = functools.partial(max, 10)
n = max2(5, 6, 7)
print(n)
