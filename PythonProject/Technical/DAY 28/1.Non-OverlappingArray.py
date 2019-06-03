# -*- coding: utf-8 -*-
"""
Given an unsorted array of integers. The task is to find any two non-overlapping pairs whose sum is equal. Two pairs are said to be non-overlapping if all the elements of the pairs are at different indices. That is pair (Ai Aj) and pair (Am An) are said to be non-overlapping if i ≠ j ≠ m ≠ n.
"""
from itertools import permutations
import itertools
sums=[]
all_pairs=[]
li=list(map(str,input().split()))
li1=li
li1=list(map(int,li1))
li2=list(permutations(li,2))
for i in li2:
    v=list(''.join(itertools.chain(*i)))
    v=list(map(int,v))
    all_pairs.append(v)
for i in all_pairs:
    sums.append(sum(i))
pairs=[]
for i in sums:
    for j in all_pairs:
        if i==sum(j):
            if j[0] in li1:
                if j[1] in li1:
                    li1.remove(j[0])
                    li1.remove(j[1])
                    pairs.append(j)
    if len(pairs)%2==0:
        continue
    else:
        pairs=[]
if len(pairs)==0:
    print(0)
else:
    for i in pairs:
        print(*i)            
            
