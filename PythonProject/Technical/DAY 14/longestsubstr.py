# -*- coding: utf-8 -*-
"""
Given a binary string. We need to find the length of longest balanced sub string. A sub string is balanced if it contains equal number of 0 and 1.
"""
s=input()
count1=s.count('1')
count0=s.count('0')
value=min(count1,count0)
print(2*value)
