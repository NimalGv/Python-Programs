# -*- coding: utf-8 -*-
"""
Given a character array arr[] containing only lowercase English alphabets the task is to print the maximum length of the subarray such that the first and the last element of the sub-array are same.
"""
def subarray(list1):
    sublist = [[]]
    for i in range(len(list1) + 1):
        for j in range(i + 1, len(list1) + 1):
            sub = list1[i:j] 
            sublist.append(sub)
    return sublist 


li=list(map(str,input().split()))
li2=subarray(li)
go=True
while go:
    target=max(li2)
    if target[0]==target[len(target)-1]:
        print(len(target))
        go=False
    else:
        target.remove(max(li2))