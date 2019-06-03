# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:12:38 2019

@author: admin
"""
import time
start=time.time()


array=[47, 85, 2, 8, 92, 35, 92, 89, 20, 58, 587, 24]

print(array)

size=len(array)
for i in range(0, size, +2):
    for j in range(0, size-2-i, +2):
        if(array[j]<array[j+2]):
            array[j], array[j+2]=array[j+2], array[j]
            
for i in range(0, size, +2):
    for j in range(1, size-2-i, +2):
        if(array[j]>array[j+2]):
            array[j], array[j+2]=array[j+2], array[j]

print(array)


end=time.time()
print("\nExecution Time : ",end-start)
