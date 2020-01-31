#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:39:00 2020
Purdue account name: vvunnava
Github account name: gargeyavunnava
Exercise 6.8, thinkpython 2e

Program description: a function 'mysqrt' is defined to find the square root of 
a number using the newtons method
"""

import math # to use the inbuilt square rootfunction in math library

"""
The mysqrt function takes a number as input to find its square root.
the starting esimate used in the netown method is x=3 and the difference 
between two calucualted square roots by two consecutive iterations is defined 
as epsilon =  0.0000000000000001
the function uses a while loop where the esitmate is updated after each iteration.
the while loop is ended using the inbuilt 'break'statement of python when the 
calculated value is smaller that epsilon.
"""
def mysqrt(a):
    x=3
    epsilon=0.0000000000000001
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return x

"""
test-square_root function is defined to print the square root values of the 
numbers 1 through 9 calculated using mysqrt function and comapre it with 
the values calculated by sqrt function in 'math' library. It also prints 
the difference between them.
A for loop is used 9 times to run the funtions mysqrt and math.sqrt 9 times. 
"""
def test_square_root():
    print("a", "mysqrt(a)", "math.sqrt(a)", "diff",sep = "\t", end = "\n")
    print("-", "---------", "------------", "----",sep = "\t", end = "\n")
    for a in range(1,10):
         print("%.1f" % a, "%.12f" % mysqrt(a), "%.12f" % math.sqrt(a), (abs(mysqrt(a)- math.sqrt(a))),sep = "\t", end = "\n")
        
test_square_root()