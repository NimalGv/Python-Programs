# -*- coding: utf-8 -*-
"""
Given an unsorted array with both positive and negative elements. Find the smallest positive number missing from the array in O(n) time using constant extra space. It is allowed to modify the original array.
"""
li=list(map(int,input().split()))
i=1
while(True):
   if i in li:
       i+=1
       continue       
   else:
       break
print(i)
