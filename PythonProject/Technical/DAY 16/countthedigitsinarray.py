# -*- coding: utf-8 -*-
"""
Given an array A[] of n elements. Your task is to return an integer denoting the total number of times digit k appears in the whole array. For Example: A[]={11,12,13,14,15}, k=1 Output=6 //Count the digit 1 in the array
"""
s=''
size=int(input())
li=list(map(int,input().split()))
number=input()
for i in li:
    s+=str(i)
print(s.count(number))