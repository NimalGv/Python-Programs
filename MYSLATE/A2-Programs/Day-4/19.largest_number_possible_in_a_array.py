# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:49:16 2019

@author: admin
"""
import time
start=time.time()


def combine(num_1, num_2):
    len_2=len(str(num_2))
    num_1*=pow(10,len_2)
    num_1+=num_2
    return num_1

def compare(num_1, num_2):
    if(combine(num_2, num_1)>combine(num_1, num_2)):
        return True
    return False

li=[18,23,12,30,1, 6,72,5,8,19]
run=len(li)-1
print(li)
for j in range(len(li)-1):
    for i in range(run):
        if(compare(li[i], li[i+1])):
            li[i], li[i+1]=li[i+1], li[i]
            print(li)
    run-=1
        
for i in range(0,len(li)):
    print(li[i], end="")


end=time.time()
print("\nExecution Time : ",end-start)
