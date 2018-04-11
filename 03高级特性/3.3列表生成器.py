#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-15 下午9:37
# @Author  : congl
# @Site    : 
# @File    : 3.3列表生成器.py
# @Software: PyCharm

import os

# 1、生成[1x1, 2x2, 3x3, ..., 10x10]
a = [x * x for x in range(1, 11)]
print(a)
b = [x * x for x in range(1, 11) if x % 2 == 0]
print(b)

# 2、双重循环
c = [m + n for m in 'ABC' for n in 'XYZ']
print(c)
# 应用，列出当前目录所有文件
f = [d for d in os.listdir('.')]
print(f)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

ll = [s.lower() for s in ['A', 2, 'AGc'] if isinstance(s, str)]
print(ll)
