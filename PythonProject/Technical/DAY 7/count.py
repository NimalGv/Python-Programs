# -*- coding: utf-8 -*-
"""
program to read a string and count total number of digits, alphabets and special characters.
"""
s=input()
digit=0
alpha=0
characters=0
for i in s:
    if(i.isdigit()):
        digit+=1
    if(i.isalpha()):
        alpha+=1
    elif not i.isdigit():
        characters+=1

print(digit)
print(alpha)
print(characters)    
