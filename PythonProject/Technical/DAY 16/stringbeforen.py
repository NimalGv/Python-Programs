# -*- coding: utf-8 -*-
"""Print the strings before \n"""
s=input()
for i in s:
    if i=="\\":
        break
    else:
        print(i,end="")
