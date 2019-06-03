# -*- coding: utf-8 -*-
"""
Given a number N, you need to write a program that finds the sum of digits of the number till the number becomes a single digit and then check whether the number is Prime/Non-Prime
"""
def sum_of_number(number):
    sum=0
    if len(number)==1:
        return number
    else:
        for i in number:
            sum+=int(i)
        return sum_of_number(str(sum))

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


n=int(input())
str_no=str(n)
int(sum_of_number(str_no))
no=int(sum_of_number(str_no))
if check_prime(no):
    print("P")
else:
    print("NP")