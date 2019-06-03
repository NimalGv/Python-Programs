# -*- coding: utf-8 -*-
"""
Given a string of ‘0’, ‘1’ and ‘2’. The task is to find the minimum number of replacements such that the adjacent characters are not equal.
"""
s=input()
count=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
print(count)