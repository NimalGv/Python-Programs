# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:25:42 2019

@author: admin
"""
import time
start=time.time()


li=[1, 1, 4, 2, 3, 2, 4, 3, 5, 5, 77, 55, 77]
xor=0
for i in li:
    xor^=i
print(xor)

for i in li:
    if li.count(i)==1:
        print(i)
        break
    
end=time.time()
print("\nExecution Time : ",end-start)
