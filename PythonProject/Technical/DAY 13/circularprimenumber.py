# -*- coding: utf-8 -*-
"""
A prime number is a Circular Prime Number if all of its possible rotations are itself prime numbers. Now given a number N check if it is circular Prime or Not.
"""
def rotate(number):
    new_no=number+number
    li=[]
    string=''
    for i in range(len(number)):
        for j in range(len(number)):
            string+=new_no[i+j]
        li.append(string)
        string=''
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
no1=str(no)
count=0
li=rotate(no1)
for i in range(len(li)):
    if check_prime(int(li[i])):
        count+=1
    else:
        break
if count==len(li):
    print(1)
else:
    print(0)