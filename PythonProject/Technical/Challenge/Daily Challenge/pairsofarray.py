# -*- coding: utf-8 -*-
"""
Given an array of ‘n’ positive integers, count number of pairs of integers in the array that have the sum divisible by 4.
"""

1234567
n=int(input())
li=list(map(int,input().split()))
li2=li[1:]
li3=[]
li4=[]
count=0
for i in li:
    for j in li2:
        if (i+j)%4==0:
            li3.append(i+j)

for i in li3:
    if i not in li4:
        li4.append(i)
print(len(li4))