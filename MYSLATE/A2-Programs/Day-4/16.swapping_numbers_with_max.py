# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:07:14 2019

@author: admin
"""
import time
start=time.time()


li=[10, 16, 17, 90, 56, 78, 8, 64, 88, 67, 283, 91, 100, 109, 143, 210, 30, 186, 203, 186, 98 ]
max_val=li[len(li)-1]
for i in range(len(li)-2,-1,-1):
    if(li[i]<max_val):
        li[i]=max_val
    else:
        max_val=li[i]
print(li)
        
    


end=time.time()
print("\nExecution Time : ",end-start)
