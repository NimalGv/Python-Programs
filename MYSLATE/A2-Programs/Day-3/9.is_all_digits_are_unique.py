# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 20:37:14 2019

@author: admin
"""
import time
start=time.time()



def unique(number):
    res=0
    while(number):
        digit=number%10
        mask=1<<digit
        if((res & mask)==mask):
            return False
        res=res|mask
        number//=10
    return True



end=time.time()
print("Execution Time : ",end-start)
