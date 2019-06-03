# -*- coding: utf-8 -*-
"""
Given a number n, check if it is Full Prime or not. Note : A full prime number is one in which the number itself is prime and all its digits are also prime.
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


number=input()
check=True
reach=False
is_no_prime=check_prime(int(number))
if is_no_prime:
    reach=True
    for i in number:
        if not check_prime(int(i)):
            check=False
            break
if reach:
    if check:
        print("Yes")
    else:
        print("No")
else:
    print("No")
            
    

