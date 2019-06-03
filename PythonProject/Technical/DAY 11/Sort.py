# -*- coding: utf-8 -*-
"""
You need to sort elements of an array where the array can be of following data-types: • Integer • String • floating number Your task is to complete the given two functions: sortArray() and printArray()
"""
def sortlist(li):
    li.sort()
    return li

def printlist(li):
    print(*li)

testcase=int(input())
while testcase!=0:
    p,q=map(int,input().split())
    if q==1:
        li=list(map(int,input().split()))
    if q==2:
        li=list(map(str,input().split()))
    if q==3:
        li=list(map(float,input().split()))
    li=sortlist(li)
    printlist(li)
    testcase-=1
