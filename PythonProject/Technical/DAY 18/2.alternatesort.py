# -*- coding: utf-8 -*-
"""
Alternate sort in unsorted array. Sort the odd position element in descending order and even position in asceding order
"""
size=input()
array=list(map(int,input().split()))
for i in range(0,len(array)-2,+2):
    for j in range(i+2,len(array),+2):
        if array[i]<array[j]:
            array[i],array[j]=array[j],array[i]
for i in range(1,len(array)-2,+2):
    for j in range(i+2,len(array),+2):
        if array[i]>array[j]:
            array[i],array[j]=array[j],array[i]
print(*array)
