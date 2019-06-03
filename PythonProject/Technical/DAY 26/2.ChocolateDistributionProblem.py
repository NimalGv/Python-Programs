# -*- coding: utf-8 -*-
"""
Given an array A[] of N integers where each value represents number of chocolates in a packet. Each packet can have variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 1. Each student gets one packet. 2. The difference between the number of chocolates given to the students in packet with maximum chocolates and packet with minimum chocolates is minimum.
"""
size=input()
li=list(map(int,input().split()))
limit=int(input())
li.sort()
li2=[]
for i in range(len(li)-limit+1):
    li2.append(li[i:i+limit])
li3=[]
for i in li2:
    li3.append(i[len(i)-1]-i[0])
print(min(li3))