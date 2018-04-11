#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-15 下午8:01
# @Author  : congl
# @Site    : 
# @File    : 3.1切片.py
# @Software: PyCharm

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 从索引0开始取，直到索引3为止，但不包括索引3
# 如果第一公众号是0可以省略
print(L[0:3])
print(L[:3])
# 倒数切片
print(L[-2:])

L = list(range(100))
# 前11-20个数
print(L[10:20])
# 前10个数，每两个取一个
print(L[:10:2])
# 所有数，每10个取一个：
print(L[::10])

# tuple也是可以做切片，但是切后的仍是tuple
# 字符串也可以做切片，替代java中的substring
