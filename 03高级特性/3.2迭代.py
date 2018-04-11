#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-15 下午8:11
# @Author  : congl
# @Site    : 
# @File    : 3.2迭代.py
# @Software: PyCharm

from collections import Iterable

# 1、字典迭代
D = {'A': 1, 'B': 2, 'C': 3}
for key in D:
    print(key)
    print(D.get(key))

for val in D.values():
    print(val)

for key, val in D.items():
    print("key:", key, "value:", val)

# 2、字符串迭代
for ch in 'ABC':
    print(ch)

# 3、使用下标迭代
for i, value in enumerate({'A', 'B', 'C'}):
    print('第%d个元素为%s' % (i + 1, value))

# 4、判断对象是否可迭代

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(34, Iterable))


def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    min_val = L[0]
    max_val = L[0]
    for v in L:
        if v > max_val:
            max_val = v
        if v < min_val:
            min_val = v

    return (min_val, max_val)


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
