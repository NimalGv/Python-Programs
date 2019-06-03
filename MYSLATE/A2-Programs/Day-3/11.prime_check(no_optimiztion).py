# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:20:46 2019

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

print(is_Prime(99999997))

end=time.time()
print("\nExecution Time : ",end-start)
