# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:42:01 2019

@author: admin
"""
import time
import math
start=time.time()


def is_Prime(number):
    for i in range(2,int(math.sqrt(number))+1):
        if(number%i==0):
            return False
    return True

limit=10000000
count=0
for i in range(2,limit+1):
    if(is_Prime(i)):
        count+=1
print(count)


end=time.time()
print("\nExecution Time : ",end-start)
