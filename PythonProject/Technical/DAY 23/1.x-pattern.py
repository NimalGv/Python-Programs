# -*- coding: utf-8 -*-
"""
Given a number with odd number of digits, print the number X format.
"""
s=input()
point=0
for i in range(0,len(s)):
    for j in range(0,len(s)):
        if j==i:
            print(s[j],end="")
            if j==len(s)//2:
                point+=1
        elif j==len(s)-1-point:
            print(s[j],end="")
            point+=1
        else:
            print(" ",end="")
    print()
