# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:53:55 2019

@author: admin
"""
import time
import math
start=time.time()


def is_Prime(number):
    for i in range(3,int(math.sqrt(number))+1,+2):
        if(number%i==0):
            return False
    return True

limit=10000000
count=1
for i in range(3,limit+1,+2):
    if(is_Prime(i)):
        count+=1
print(count)


end=time.time()
print("\nExecution Time : ",end-start)
