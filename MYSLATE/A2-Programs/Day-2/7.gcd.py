# -*- coding: utf-8 -*-
"""
Finding gcd
"""

def gcd(no1,no2):
    if(no1>no2):
        no2,no1=no1,no2
    if(no2%no1==0):
        return no2
    for i in range(no1//2,1,-1):
        if(no2%i==0 and no1%i==0):
            return i
    return 0
