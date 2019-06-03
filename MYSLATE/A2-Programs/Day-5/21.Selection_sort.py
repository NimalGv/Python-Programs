# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 18:37:53 2019

@author: admin
"""
import time
start=time.time()


array=[34, 78, 12, 45, 23, 95, 11, 66, 15, 42, 51, 88, 33, 90, 47]
    #  0   1   2   3    4   5   6   7   8   9  10  11  12  13  14

min_val=array[0]

for i in range(0, len(array)-1):
    min_pos=i
    for j in range(i+1, len(array)):
        if(array[min_pos] > array[j]):
            min_pos=j
    array[i], array[min_pos]=array[min_pos], array[i]

print(*array)

end=time.time()
print("\nExecution Time : ",end-start)
