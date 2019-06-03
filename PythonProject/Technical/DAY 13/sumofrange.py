# -*- coding: utf-8 -*-
"""
Given an array arr of size N. The task is to return the sum in the given range a and b. Note: 0-based indexing is used.
"""
size=int(input())
range1,range2=map(int,input().split())
li=list(map(int,input().split()))
print(sum(li[range1:range2+1]))
