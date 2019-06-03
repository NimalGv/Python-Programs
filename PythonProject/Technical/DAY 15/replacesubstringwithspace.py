# -*- coding: utf-8 -*-
"""
Given a string and a substring, the task is to replace all occurrences of the substring with space,also need to remove trailing and leading spaces created due to this.
"""
s1=input()
s2=input()
'''
count=s1.count(s2)
s=s1.replace(s2,' ',count)
print(s.strip())'''
s=s1.split(s2)
for i in s:
    if i!='':
        print(i,end=" ")