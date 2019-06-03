# -*- coding: utf-8 -*-
"""
program to find the sum of series 1 + 11 + 111 + 1111 + ... N terms.
"""

def series_sum(number):
    if number==1:
        return 1
    return number+series_sum(number-pow(10,len(str(number))-1))
   
n=int(input())
number=int(str('1'*n))
print(series_sum(number))