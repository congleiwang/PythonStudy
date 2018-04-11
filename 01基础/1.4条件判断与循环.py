#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-15 下午5:13
# @Author  : congl
# @Site    : 
# @File    : 1.4条件判断与循环.py
# @Software: PyCharm

# if条件

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
#     低于18.5：过轻
#     18.5-25：正常
#     25-28：过重
#     28-32：肥胖
#     高于32：严重肥胖
#
# 用if-elif判断并打印结果：

bmi_val = 80.5 / 1.75 ** 2
if bmi_val <= 18.5:
    print("过轻")
elif bmi_val <= 25:
    print('正常')
elif bmi_val <= 28:
    print('过重')
elif bmi_val <= 32:
    print('肥胖')
else:
    print('严重肥胖')

# 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in range(1, 101, 1):
    sum = x + sum
print(sum)

n = 99
sum = 0
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
