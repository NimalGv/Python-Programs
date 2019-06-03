# -*- coding: utf-8 -*-
"""
program  to find out the maximum difference between any two elements such that larger element appears after the smaller number.
"""
dif=0
prev=0
li=list(map(int,input().split()))
maximum=max(li)
for i in li:
    if i!=maximum:
        prev=dif
        dif=maximum-i
        if prev>dif:
            maxdif=prev
        else:
            maxdif=dif
    else:
        break
print("The Maximum difference between two elements in the array is: "+str(maxdif))
