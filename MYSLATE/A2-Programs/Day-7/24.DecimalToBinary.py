# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:45:22 2019

@author: admin
"""
import time
start=time.time()


def To_binary(number):
    if(number<2):
        return number
    return To_binary(number//2)*10+number%2

print(To_binary(26))


end=time.time()
print("\nExecution Time : ",end-start)
