# -*- coding: utf-8 -*-
"""
Given two binary strings that represent value of two integers, find the product of two strings. For example, if the first bit string is “1100” and second bit string is “1010”, output should be 120.
"""
s1,s2=map(str,input().split())
print(int(s1,2)*int(s2,2))
