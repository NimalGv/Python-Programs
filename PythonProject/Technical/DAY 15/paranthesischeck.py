# -*- coding: utf-8 -*-
"""
Write a Program to check if expression is correctly parenthesized.
"""
s=input()
li=[]
for i in s:
    if i=='(' or i==')':
        li.append(i)

li.reverse()
li1=li.copy()
for i in li:
    if i==')' :
        if '(' in li1:
            li1.remove(i)
            li1.remove('(')
if len(li1)==0:
    print("Expression is valid")
else:
    print("Expression is invalid")
    