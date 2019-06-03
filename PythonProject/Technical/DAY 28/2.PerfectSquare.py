# -*- coding: utf-8 -*-
"""
Given a integer n,find how many digits removed from the number to make it a perfect square.
"""
import math
from itertools import combinations
import itertools

min_len=[]
comb=[]
reach=False

def is_perfect_square(n):
    value=int(math.sqrt(n))
    if value*value==n:
        return True
    else:
        return False

def combination(string):
    global reach
    for i in range(1,len(string)):
        li=list(combinations(string,i))
        for i in li:
            v="".join(itertools.chain(*i))
            comb.append(v)
        li=[]
    comb.append(str(Number))
    comb.sort(reverse=True)
    for i in comb:
        if is_perfect_square(int(i)):
            print(len(str(Number))-len(i))
            reach=True
            break
        
        
Number=int(input())
combination(str(Number))
if not reach:
    print(-1)

