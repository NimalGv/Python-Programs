# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:40:44 2019
123
@author: admin
"""
import time
start=time.time()

def decimal_to_NBase(num, base):
    i=0
    conv_num=0
    while(num):
        digit=num % base
        conv_num=digit*pow(10, i)+conv_num
        num//=base
        i+=1
    return conv_num

def NBase_to_decimal(num, base):
    i=0
    conv_num=0
    while(num):
        digit=num%10
        conv_num=digit*pow(base, i)+conv_num
        num//=10
        i+=1
    return conv_num
        
def xor_NBase(num_1, num_2, base):
    conv_num=0
    i=0
    while(num_1 or num_2):
        digit_1=num_1%10
        digit_2=num_2%10
        result=digit_1+digit_2;
        result%=base
        conv_num=result*pow(10, i)+conv_num
        num_1//=10
        num_2//=10
        i+=1
    return conv_num
    
li=[123,113,145,134,134,113,92,113,123,123,145,145, 134]
xor=0
result=0

for i in li:
    result=xor_NBase(result, decimal_to_NBase(i, 3), 3)

print(NBase_to_decimal(result, 3))


end=time.time()
print("\nExecution Time : ",end-start)
