# -*- coding: utf-8 -*-
"""
Given a string, recursively remove adjacent duplicate characters from string. The output string should not have any adjacent duplicates.
"""
#acaaabbbacdddd

s=input()
comp=s[0]
v='0'
run=True
came=False
li=[]
for i in s:
    li.append(i)
while(run):
    li1=li.copy()
    for i in range(0,len(li1)-1):
        if li1[i]==comp and li[i+1]==comp:
            li[i]='0'
            li[i+1]='0'
        else:
            comp=s[i+1]
    while(v in li):
        came=True
        li.remove('0')
    if came:
        run=True
    else:
        run=False
    came=False
for i in li:
    print(i,end="")      
    
