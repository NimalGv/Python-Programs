# -*- coding: utf-8 -*-
"""
To find the factors of the numbers given in an array and to sort the numbers in descending order according to the factors present in it.
"""
def no_of_factors(number):
    count=0
    for i in range(1,number+1):
        if number%i==0:
            count+=1
    return count

size=int(input())
li=list(map(int,input().split()))
l1=[]
for i in li:
    l1.append(no_of_factors(i))
for i in range(size):
    print(li[l1.index(max(l1))],end=" ")
    li.remove(li[l1.index(max(l1))])
    l1.remove(max(l1))