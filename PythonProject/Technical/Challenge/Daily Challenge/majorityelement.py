# -*- coding: utf-8 -*-
"""
A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element). Write a function which takes an array and emits the majority element (if it exists), otherwise prints -1.
"""
size=input()
li1=list(map(int,input().split()))
li2=[]
reach=False
for i in li1:
    if i not in li2:
        li2.append(i)
for i in li2:
    if li1.count(i)>len(li1)//2:
        print(i,end=" ")
        reach=True
if not reach:
    print("-1")
