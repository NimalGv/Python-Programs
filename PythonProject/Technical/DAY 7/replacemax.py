# -*- coding: utf-8 -*-
"""
program  to replace every element with the greatest element on its right side
"""

def replace(l):
    m=max(l)
    r=l.index(m)
    
    for i in range (r+1):
        if(i==r):
            l[i]=0
        else:
            l[i]=m 
            ol.append(l[i])
    if r==len(l)-1:
        ol.append(l[len(l)-1])
        return 0
    return replace(l[r:])
        

ol=[]
li=list(map(int,input().split()))
replace(li)
print(" ",end="")
print(*ol)

