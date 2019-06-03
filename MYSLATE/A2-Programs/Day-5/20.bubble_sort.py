# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 18:13:53 2019

@author: admin
"""
import time
start=time.time()


array=[34, 78, 12, 45, 23, 95, 11, 66, 15, 42, 51, 88, 33, 90, 47]
    #  0   1   2   3    4   5   6   7   8   9  10  11  12  13  14
swapped=True

for i in range(0, len(array)):
    if(swapped):                            #2'nd optimiztion
        swapped=False
        for j in range(0, len(array)-1-i):  #1'st optimization
            if(array[j] > array[j+1] ):
                array[j], array[j+1]=array[j+1], array[j]
                swapped=True
            
print(*array)


end=time.time()
print("\nExecution Time : ",end-start)
