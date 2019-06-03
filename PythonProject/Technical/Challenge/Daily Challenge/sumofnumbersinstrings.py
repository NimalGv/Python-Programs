# -*- coding: utf-8 -*-
"""
Given a string containing alphanumeric characters, calculate sum of all numbers present in the string.
"""
import re
s=input()
li=re.split('[^0-9]',s)
li2=[]
for i in li:
    if i!='':
        li2.append(int(i))
print(sum(li2))

