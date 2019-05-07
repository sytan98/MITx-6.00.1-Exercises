# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 10:01:48 2019

@author: sytan
"""

Number = input('Please think of a number between 0 and 100!')
low = 0
high = 100
guess = (low + high)/2

while guess != Number:
    print('Is your secret number %d?'% guess)
    Check = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if Check == 'c':
        print('Game over. Your secret number was: %d' % guess)
        break
    elif Check =='h':
        high = guess
        guess = (low+high)/2
    elif Check =='l':
        low = guess
        guess = (low+high)/2
    else:
        print('Sorry, I did not understand your input.')
