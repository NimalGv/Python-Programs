# -*- coding: utf-8 -*-
"""
floyds triangle
"""
number=1
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(str(number),end=" ")
        number+=1
    print()
