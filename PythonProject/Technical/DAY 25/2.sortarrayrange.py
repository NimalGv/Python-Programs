# -*- coding: utf-8 -*-
"""
Given an array arr[] of N integers and an index range [a b]. The task is to sort the array in this given index range i.e. sort the elements of the array from arr[a] to arr[b] while keeping the positions of other elements intact and print the modified array. Note: There is no relation between a and b i.e. a can be less than equal to or greater than b. Also 0 ≤ a b < N
"""
li=list(map(int,input().split()))
a,b=map(int,input().split())
Done=False
for i in range(len(li)):
    if i>=min(a,b) and i<=max(a,b):
        if not Done:
            li2=li[min(a,b):max(a,b)+1]
            li2.sort()
            print(*li2,end=" ")
            Done=True
    else:
        print(li[i],end=" ")
        
