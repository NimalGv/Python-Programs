# -*- coding: utf-8 -*-
"""
Given an array of integers, The task is to find another integer such that, if all the elements of the array are subtracted individually from the number , then the sum of all the differences should add to 0. Example - Input: arr[] = {1, 2, 3} Output: 2 Explanation: 
Substracting all the elements of arrays from 2, The sum of difference is: 1 + 0 + (-1) = 0.
"""
li=list(map(int,input().split()))
limit=max(li)
total=0
reach=False
for i in range(1,limit+1):
    for j in li:
        total+=j-i
    if total==0:
        print(i)
        reach=True
        break
    total=0
if not reach:
    print('-1')
