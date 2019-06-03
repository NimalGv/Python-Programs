# -*- coding: utf-8 -*-
"""
Write a Program to reverse every word of given string
"""
li=list(map(str,input().split()))
for i in li:
    print(i[::-1],end="")