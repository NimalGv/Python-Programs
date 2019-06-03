# -*- coding: utf-8 -*-
"""
Find the number of common divisors of p and q.
"""
no1,no2=map(int,input().split())
limit=min(no1,no2)
count=0
for i in range(1,limit+1):
    if no1%i==no2%i==0:
        count+=1
print(count)