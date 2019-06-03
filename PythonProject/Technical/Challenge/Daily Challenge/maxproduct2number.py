# -*- coding: utf-8 -*-
"""
Given an array with all elements greater than or equal to zero. Return the maximum product of two numbers possible.
"""
size=input()
l1=list(map(int,input().split()))
l2=[]
for i in range(len(l1)-1):
    for j in range(i+1,len(l1)):
        l2.append(l1[i]*l1[j])
print(max(l2))
