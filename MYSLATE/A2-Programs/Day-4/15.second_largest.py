# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:54:18 2019

@author: admin
"""
import time
start=time.time()


li=[10, 16, 17, 90, 56, 78, 8, 64, 88, 67, 83, 91, 100, 109, 143, 2100, 30, 186, 203, 186, 298 ]
max_1=0
max_2=0
for i in li:
    if i>max_1:
        max_2=max_1
        max_1=i
    elif i>max_2:
        max_2=i
print("Second Largest: ",max_2)

end=time.time()
print("\nExecution Time : ",end-start)
