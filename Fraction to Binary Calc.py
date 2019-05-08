# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:03:34 2019

@author: sytan
"""
#Calculator to convert fractions to binary form
"""
Common method is to Multiply by two, take decimal as the digit, take the fraction \
as the starting point for the next step, repeat until you either get to 0 or a periodic number,
read the number starting from the top - the first result is the first digit after the comma.
This method does it differently and multiplies fraction by 2 till it reaches a whole number.
"""
x = float(input('Enter a decimal number between 0 and 1: '))

p = 0
while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x))) #minus nearest whole number to get remainder after dividing by 1
    p += 1

#Multiply by a power of 2 big enough to convert into whole number
num = int(x*(2**p))
print(num)
result = ''

#Check if number is zero
if num == 0:
    result = '0'
    
#Converting whole number to binary by dividing by 2
while num > 0:
    result = str(num%2) + result
    num = num //2

#Adding zeros at the front
for i in range(p - len(result)):
    result = '0' + result
    
print(result)
result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))