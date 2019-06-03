# -*- coding: utf-8 -*-
"""
A simple method would be to traverse the array and store frequencies of its elements in a map. Later, print elements that have even count in the map. The solution takes O(n) time but requires extra space for storing frequencies. Below is an interesting method to solve this problem using bitwise operators.
"""

li1=list(map(int,input().split()))
li2=[]
for i in li1:
    if i not in li2:
        li2.append(i)
for i in li2:
    if li1.count(i)%2==0:
        print(i,end=" ")
