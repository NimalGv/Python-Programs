# -*- coding: utf-8 -*-
"""
program to find out the maximum difference between any two elements such that larger element appears after the smaller number.
"""

li=list(map(int,input().split()))
max_value=max(li)
max_index=li.index(max_value)
li=li[0:max_index]
min_value=min(li)
print(max_value-min_value)