# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:41:23 2019

@author: admin
"""
import time
start=time.time()


row=9

for i in range(1, row+1):
    for space in range(row-1, i-1, -1):
        print(" ", end=" ")
    for forward in range(1, i+1):
        print(forward, end=" ")
    for reverse in range(i-1, 0, -1):
        print(reverse, end=" ")
    print() 

for i in range(row-1, 0, -1):
    for space in range(1, row-i+1):
        print(" ", end=" ")
    for forward in range(1, i+1):
        print(forward, end=" ")
    for reverse in range(i-1, 0, -1):
        print(reverse, end=" ")
    
    print()   


end=time.time()
print("\nExecution Time : ",end-start)
