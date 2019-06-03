# -*- coding: utf-8 -*-
"""
Given a sorted array arr[] and a number x write a function that counts the occurrences of x in arr[]. Expected time complexity is O(Logn)
"""

li=list(map(int,input().split()))
x=int(input())
if x in li:
    print(li.count(x))
else:
    print("-1")