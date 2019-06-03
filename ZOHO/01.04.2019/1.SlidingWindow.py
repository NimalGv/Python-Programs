# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 22:15:24 2019

@author: admin
"""
import time




size=int(input())
array=list(map(int, input().split()))
window_size=int(input())

start=0
end=window_size

for i in range(0, len(array)):
    max_val=-110
    if(start!=size-window_size+1):
        for j in range(start, start+window_size):
            if(array[j]>max_val):
                max_val=array[j]
        print(max_val, end=" ")
        start+=1
    else:
        break
        


start=time.time()
end=time.time()
print("\nExecution Time : ",end-start)
