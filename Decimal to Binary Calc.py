# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:47:06 2019

@author: sytan
"""

num = int(input('What is the number'))

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result = '-' + result
    
print(result)