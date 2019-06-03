# -*- coding: utf-8 -*-
"""
Write a program to eliminate/remove first character of each word from a string
"""
li=list(map(str,input().split()))
for i in li:
    print(i[1:],end=" ")
