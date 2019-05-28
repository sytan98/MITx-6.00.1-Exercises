# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:42:03 2019

@author: sytan
"""
#Solution to the Tower of Hanoi Problem with recursion
"""
Rules: Move only one disk at a time. 
A larger disk may not be placed ontop of a smaller disk. 
All disks, except the one being moved, must be on a peg.
"""

def printMove(fr, to):
    print('Move one piece from position ' + str(fr) + ' to position ' + str(to))

#Resursion to 
def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)  #Move top to spare
        Towers(1, fr, to, spare)    #Move Bottom one to destination
        Towers(n-1, spare, to, fr)  #Move top piece to destination

#Getting input from user
n, fr, to, spare = input('Please key in your number of stack, followed by \
                         position of source, position of destination, \
                         postion of spare, separated by commas: ').split(",")

Towers(int(n), int(fr), int(to), int(spare))



