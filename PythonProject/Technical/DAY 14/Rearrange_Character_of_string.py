# -*- coding: utf-8 -*-
"""
Given a string str containing lowercase alphabets (a – z). The task is to print the string after rearranging some characters such that the string becomes non-palindromic.
"""
from itertools import permutations

def check_palindrome(s):
    s1=s[::-1]
    if s1==s:
        return True
    else:
        return False
    
def combinations(s):
    l=[]
    li=permutations(s)
    for i in list(li):
        l.append("".join(i))
    return l

s=input()
reach=False
l=combinations(s)
l.sort()
for i in l:
    if not check_palindrome(i):
        print(i)
        reach=True
        break
if not reach:
    print('-1')
