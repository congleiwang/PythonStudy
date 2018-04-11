#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-15 下午9:52
# @Author  : congl
# @Site    : 
# @File    : 3.4生成器.py
# @Software: PyCharm

# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 1、使用for创建生成器
# 把一个列表生成式的[]改成()
g = (x * x for x in range(100000000))
print(g)

for n in g:
    print(n)
    if (n == 100):
        break


# 2、使用函数创建生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

f = fib(6)
print(next(f))
print(next(f))
