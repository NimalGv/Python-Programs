# -*- coding: utf-8 -*-
"""
Program to print pyramid using *
"""
no=int(input())
tno=no
pattern=1
for i in range(no):
    for j in range(1,no-i+1):
        if j==tno:
            for k in range(1,pattern+1):
                print("*",end=" ")
            pattern+=2
        else:
            print(" ",end=" ")
    print()
    tno-=1
            
