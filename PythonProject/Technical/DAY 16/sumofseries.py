# -*- coding: utf-8 -*-
'''Given a series as shown below:

1 2

3 4 5 6

7 8 9 10 11 12

13 14 15 16 17 18 19 20

..........................

............................

(so on)

You are given a number N, you need to write a program to find the sum of all elements in the N-th row of above series.
'''
no=int(input())
start=no*(no-1)+1
print(sum([i for i in range(start,start+no*2)]))