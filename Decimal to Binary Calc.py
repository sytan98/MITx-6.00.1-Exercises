# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:47:06 2019

@author: sytan
"""
#Calculator to convert integer to binary form
num = int(input('What is the number? '))

#Check if number is negative
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

#Check if number is zero
result = ''
if num == 0:
    result = '0'
    
#Converting num to binary by dividing by 2
while num > 0:
    result = str(num%2) + result
    num = num//2
"""
def binary(num, result):
    while num > 0:
        result = str(num%2) + result
        num = num//2
    return result
binary(num, result)"""

#Changing Negative number to Negative
if isNeg:
    result = '-' + result
    
print(result)