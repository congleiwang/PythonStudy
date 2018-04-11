#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-26上午10:06
# @Author  : congl
# @Site    : 
# @File    : 4.2返回函数.py
# @Software: PyCharm

# 通过返回函数实现闭包，闭包中如果有循环，这循环中的变量会在返回函数后调用函数钱执行完成。
def createCounter():
    result = 0

    def counter():
        nonlocal result
        result += 1
        return result

    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
