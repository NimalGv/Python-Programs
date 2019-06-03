# -*- coding: utf-8 -*-
"""
Given an array of N positive integers. Count the number of pairs whose sum exists in the given array. While repeating pairs will not be counted again. And can’t make a pair using same position element. Eg : (2 1) and (1 2) will be considered as only one pair.
"""


def pair_generate(li):
    li1=[]
    temp=[]
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if li[i]+li[j] in li:
                temp.extend([li[i],li[j]])
                temp.sort()
                li1.append(temp)
                temp=[]
    return li1

def distinct_pair(li):
    li1=[]
    for i in li:
        if i not in li1:
            li1.append(i)
    return len(li1)


li=list(map(int,input().split()))
print(distinct_pair(pair_generate(li)))
                
        