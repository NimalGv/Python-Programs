# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:07:18 2019

@author: admin
"""
import time
start=time.time()


array=[34, 78, 12, 45, 23, 95, 11, 66, 15, 42, 51, 88, 33, 90, 47]
    #  0   1   2   3    4   5   6   7   8   9  10  11  12  13  14

for sort in range(0, len(array)-1):
    for unsorted in range(sort+1, 0, -1):
        if(array[unsorted]<array[unsorted-1]):
            array[unsorted], array[unsorted-1]=array[unsorted-1], array[unsorted]
 
print(*array)           

end=time.time()
print("\nExecution Time : ",end-start)
