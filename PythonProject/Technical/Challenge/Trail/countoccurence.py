# -*- coding: utf-8 -*-
"""
Given an integer X within the range of 0 to 9, and given two positive integers as upper and lower bounds respectively, find the number of times X occurs as a digit in an integer within the range, excluding the bounds. Print the frequency of occurrence as output.
"""
x=input()
count=0
up,low=map(int,input().split())
for i in range(up+1,low):
    t=str(i)
    count+=t.count(x)
print(count)
