"""
Created on Fri Jan 31 11:09:28 2020
Purdue account name: vvunnava
Github account name: gargeyavunnava
Exercise 6.8, thinkpython 2e

Problem description: a function to calculate the greatest common denominator (GCD)
for two non negative integers.

GCD is applicable only to non negative integers.

the function 'gcd' is defined here that takes in 2 non negative integers as input.
it uses an if else conditional execution with recursion. recursion because it calls 
itself in the function till the base case is true. The base case is if either one 
of them is zero, then the other number is the gcd.
As mentioned in thinkpython 2e, "One way to find the GCD of two numbers is based 
on the observation that if r is the remainder when a is divided by b, then 
gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a."

in the end, the function returns the value of gcd
"""

def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

print(gcd(45,105))    #example