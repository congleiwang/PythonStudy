#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-26上午11:02
# @Author  : congl
# @Site    : 
# @File    : 4.3装饰器
# @Software: PyCharm

import time
import functools


# 装饰器：在代码运行期间动态增加功能的方式
# 装饰器本质是通过讲被装饰的函数装入到另一函数中执行，然后返回这个装饰函数。
# __name__: 函数对象内置方法，返回该函数的名称

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 把@log放到now()函数的定义处，相当于执行了now = log(now)

@log
def now():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
