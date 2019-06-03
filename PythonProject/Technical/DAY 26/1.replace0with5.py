# -*- coding: utf-8 -*-
"""
Given a number your task is to complete the function convert five which takes an integer n as argument and replaces all zeros in the number n with 5. Your function should return the converted number.
"""

def replace_0(string):
    value=string.count('0')
    string=string.replace('0','5',value)
    return int(string)

number=int(input())
print(replace_0(str(number)))