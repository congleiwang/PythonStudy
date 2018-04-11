#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-3-15 下午5:33
# @Author  : congl
# @Site    : 
# @File    : 1.5dict和set.py
# @Software: PyCharm

# 1、dict 全称dictionary，和Java中map一样，无序的key-value
soce = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(soce['Michael'])
# soce['AAA']会报错，为避免可以先用'AAA' in soce 判断。
# （1）、获取元素
print(soce.get('AAA'))
print(soce.get('AAA', '查无此人'))
# (2)新增或修改元素
soce['AAA'] = 59
soce['Bob'] = 65
# （3）、删除元素
soce.pop('Bob')
print(soce)

# 2、set 和Java的set一致,无序唯一集合
# （1）、创建set，需要一个List
s = set([1, 1, 3, 2, 2, 3])
print(s)
# (2)、添加元素
s.add(5)
# (3)、删除元素
s.remove(5)
# (4)、做交并集运算
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
