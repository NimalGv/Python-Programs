# -*- coding: utf-8 -*-
"""
Given an array A[] of N numbers and another number x, determine whether or not there exist three elements in A[] whose sum is exactly x.
"""
present=False
n,x=map(int,input().split())
l=list(map(int,input().split()))
for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
           #print(str(l[i])+"+"+str(l[j])+"+"+str(l[k])+"="+str(l[i]+l[j]+l[k]))
           if l[i]+l[j]+l[k]==x:
               present=True
               break
if present:
    print("1")
else:
    print("0")