# -*- coding: utf-8 -*-
"""
Given a number N, the task is to express N as a summation of 4 positive primes.
"""
def prime_numbers(number):
    li=[]
    for i in range(2,number+ 1):
       if i > 1:
           for j in range(2,i):
               if (i % j) == 0:
                   break
           else:
               li.append(i)
    return li

number=int(input())
li=prime_numbers(number)
Flag=False
for i in range(len(li)-3):
    if sum(li[i:i+4])==number:
        print(*li[i:i+4])
        Flag=True
        break
    else:
        Flag=False
    
if not Flag:
    print(-1)