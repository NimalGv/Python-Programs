# -*- coding: utf-8 -*-
"""
Given a string, say S, print it in reverse manner eliminating the repeated characters and spaces
"""
string=input()
li=string.split()
joined_str=''
for i in li:
    joined_str+=i
if not joined_str.isupper():
    joined_str=joined_str.casefold()

for i in joined_str:
    if joined_str.count(i)>1:
        joined_str=joined_str.replace(i,"",joined_str.count(i)-1)
print("".join(reversed(joined_str)))