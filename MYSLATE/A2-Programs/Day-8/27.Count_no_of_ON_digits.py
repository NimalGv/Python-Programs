# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:33:52 2019

@author: admin
"""
import time
start=time.time()


def count(number):
    if(number==0):
        return 0
    return count(number>>1)+(number&1)

number=15246
print(count(number),bin(number))


end=time.time()
print("\nExecution Time : ",end-start)
