# -*- coding: utf-8 -*-
"""
Given an integer input N and you have to find whether it is Anshuman’s favourite or not. A number is Anshuman’s favourite if it is either the sum or the difference of the integer 5. (5+5, 5+5+5, 5-5,5-5-5+5+5…..)
"""
no=int(input())
if no%5==0:
    print("YES")
else:
    print("NO")