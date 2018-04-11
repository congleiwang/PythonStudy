#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-27上午9:11
# @Author  : congl
# @Site    : 
# @File    : 5.1使用模块
# @Software: PyCharm

' a test module 这是模块文档，可以使用__doc__变量读取。'
__author__ = 'dalao'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello world!")
    elif len(args) == 2:
        print("Hello,%s!" % args[1])
    else:
        print("Toll man arguments")


if __name__ == '__main__':
    test()
