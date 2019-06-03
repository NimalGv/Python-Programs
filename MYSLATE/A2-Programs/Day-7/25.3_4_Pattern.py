# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:58:42 2019

@author: admin
"""
import time
start=time.time()


def pattern(position):
    if(position==1):
        return 3
    if(position==2):
        return 4
    if(position%2==0):
        return pattern((position//2)-1)*10+4
    return pattern(position//2)*10+3

for i in range(1,10):
    print(pattern(i),end=" ")


end=time.time()
print("\nExecution Time : ",end-start)
