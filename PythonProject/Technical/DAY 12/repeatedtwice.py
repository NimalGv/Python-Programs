# -*- coding: utf-8 -*-
"""
Given an array of n words. Some words are repeated twice ONLY, Need to count such words.
"""
size=int(input())
li=list(map(str,input().split()))
count=0
for i in li:
    if li.count(i)==2:
        count+=1
        li.remove(i)
print(count)