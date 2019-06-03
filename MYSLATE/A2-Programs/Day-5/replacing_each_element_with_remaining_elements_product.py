# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:25:59 2019

@author: admin
"""
import time
start=time.time()


a=[10, 8, 5, 3, 2]
product=1
for i in a:
    product*=i;
    
for i in a:
    print(product//i,end=" ")



end=time.time()
print("\nExecution Time : ",end-start)
