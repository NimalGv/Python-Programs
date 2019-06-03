# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:44:17 2019

@author: admin
"""
import time
start=time.time()

number=1256
n=number
rev_number=0
while(number):
    rev_number=rev_number|(number&1)
    number=number>>1
    rev_number=rev_number<<1
print(n, ":", bin(n), "\n", rev_number, ":", bin(rev_number))

end=time.time()
print("\nExecution Time : ",end-start)
