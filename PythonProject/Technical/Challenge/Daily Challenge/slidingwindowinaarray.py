# -*- coding: utf-8 -*-
"""
Given an array of numbers and a window of size k. Print the maximum of numbers inside the window for each step as the window moves from the beginning of the array.
"""
size=int(input())
li=list(map(int,input().split()))
k=int(input())
for i in range(len(li)-k+1):
    value=li[i]
    for j in range(1,k):
        if li[i+j]>value:
            value=li[i+j]
    print(value,end=" ")
