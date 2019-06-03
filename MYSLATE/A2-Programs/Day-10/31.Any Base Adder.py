# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:21:57 2019

@author: admin
"""
import time
start=time.time()


def base_adder(num1, num2, base):
    i=0
    result=0
    carry=0
    while(num1 or num2):
        digit1=num1%10
        digit2=num2%10
        total=digit1+digit2+carry
        print(total)
        result=(total%base)*(10**i)+result
        carry=total//base
        num1//=10
        num2//=10
        i+=1
    if(carry!=0):                      #excess carry
        result=carry*(10**i)+result
    return result

num1=45236  
num2=123456
base=7

print(base_adder(num1, num2, base))



end=time.time()
print("\nExecution Time : ",end-start)
