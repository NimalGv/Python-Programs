# -*- coding: utf-8 -*-
"""
Anagram(Integer)
"""
def check(n):
    tb=b
    while tb!=0:
        if tb%10== n:
            return True
        tb//=10
    return False

flag=1
a,b=map(int,input().split())
ta=a
while ta!=0:
    if check(ta%10):
        ta//=10
    else:
        flag=0
        break
if flag==0:
    print("Not Anagram")
else:
    print("Anagram")
    
