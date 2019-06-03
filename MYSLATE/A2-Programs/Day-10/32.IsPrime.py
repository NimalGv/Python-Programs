# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:57:36 2019

@author: admin
"""
import time
import math
start=time.time()
count=0

def is_prime(num):
    global count
    if num==1:
        return False
    if num==2 or num==3 or num==5:
        return True
    if num%2==0:
        return False
    if num%6==1 or num%6==5:
        for i in range(3, int(math.sqrt(num))+1,+2):
            if num%i==0:
                return False
        return True

for i in range(1, 101):
    if(is_prime(i)):
        count+=1
        print(i, end=" ")
print("\n", count)

end=time.time()
print("\nExecution Time : ",end-start)
