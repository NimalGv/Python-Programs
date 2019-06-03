# -*- coding: utf-8 -*-
"""
Given a string S. The task is to count and print the number of characters in the string whose ASCII values are prime.
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
    
string=input()
count=0
for i in string:
    if check_prime(ord(i)):
        count+=1
print(count)