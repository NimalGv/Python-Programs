# -*- coding: utf-8 -*-
"""
Given is a range of integers [a , b] . You have to find the sum of all the numbers in the range [ a , b] that are prime as well as palindrome .
"""
def check_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False
    
def check_palindrome(number):
    num=str(number)
    if len(num)==1:
        return True
    elif num==num[::-1]:
        return True
    else:
        return False
    
    
start,end=map(int,input().split())
primes=[]
total=0
for i in range(start,end+1):
    if check_prime(i):
        primes.append(i)
for i in primes:
    if check_palindrome(i):
        total+=i
print(total)