# -*- coding: utf-8 -*-
"""
program to replace every element with the greatest element on its right side
"""
#def replace(li):
    
l=[]
li=list(map(int,input().split()))
l=li.copy()
li.sort(reverse=True)
v=0
for i in range(len(l)):
    if bool(l.count(li[i])):
        s=l.index(li[i])
        for j in range(v,l.index(li[i])+1):
            if l[j]==li[i]:
                l[j]=0
            else:
                l[j]=li[i]
        v=s
    else:
        continue
print(*l)