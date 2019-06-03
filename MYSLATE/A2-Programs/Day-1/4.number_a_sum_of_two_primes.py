# -*- coding: utf-8 -*-
"""
 1.Any even number greater than or equal to 4 can always be written as sum of two primes
          even : even+even and odd+odd;

    2.The odd number can be written as sum of two primes if the number-2 is a prime number, because
          odd : odd+even and even+odd;
          so,    IsPrime(number-2)
          
          Goldbach's conjecture
"""
import math

def is_prime(number):
    for i in range(2,int(math.sqrt(number))+1):
        if(number%i==0):
            return False
    return True

number=int(input())
if(number>=4 and number%2==0):
    print("Can be written as sum of two primes")
elif(is_prime(number-2)):
    print("Can be written as sum of two primes")
else:
    print("Cannot be written as sum of two primes")
    



