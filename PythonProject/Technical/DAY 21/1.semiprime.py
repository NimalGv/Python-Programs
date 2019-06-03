# -*- coding: utf-8 -*-
"""
Given a positive integer n. Find whether a number is a semiprime or not. Print True if number is semiprime else False. A semiprime is a natural number that is a product of two prime numbers .
"""
def factors(number):
    li=[]
    for i in range(1,number//2+1):
        if number%i==0:
            li.append(i)
    return li

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
    
no=int(input())
close=False
factors=factors(no)
if len(factors)==1 or no==1:
    print("False")
else:
    for i in factors:
        for j in factors:
            if i*j==no:
                if check_prime(i):
                    if check_prime(j):
                        print("True")
                        close=True
                    else:
                        print("False")
                        close=True
                else:
                    print("False")
                    close=True
            if close:
                break
