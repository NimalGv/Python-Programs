# -*- coding: utf-8 -*-
"""
Given N number of strings.Find the lexicographically smallest string and the lexicographically largest string among these strings.
"""

s=input()
li=list(map(str,input().split()))
li.sort()
print(li[0],li[len(li)-1])