# -*- coding: utf-8 -*-
"""
program to accept two strings and compare. 
"""
s1=input()
s2=input()

if len(s1)>len(s2):
    print("String1 is greater")
    print(s1.upper())
    print(s2.lower())
elif len(s1)==len(s2):
    print(len(s1))
else:
    print("String2 is greater")
    print(s1.lower())
    print(s2.upper())
    

