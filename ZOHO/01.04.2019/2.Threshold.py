# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:36:54 2019

@author: admin
"""
import time
start=time.time()

count=0

def calculate(number, threshold):
    global count
    while(number>0):
        if(number-threshold >= 0):
            number-=threshold
            print("Threshold", threshold)
            count+=1
        else:
            threshold-=1
    print()

array=[67, 743, 73, 634, 89, 734, 9, 76, 90, 36, 65, 34]
threshold=12

for i in array:
    calculate(i, threshold)

print("Count", count)
    
    


end=time.time()
print("\nExecution Time : ",end-start)
