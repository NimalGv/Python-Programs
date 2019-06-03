# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:15:26 2019

@author: admin
"""
import time
start=time.time()



num=int(input())

length=len(str(num))

i=1
while(i<length):
    pos_1=i
    pos_2=i+1
    print(i, i+1)
    pos_1=(length-pos_1)+1
    pos_2=(length-pos_2)+1
     
    digit_1=(num//pow(10, pos_1-1))%10
    num=num-digit_1*pow(10, pos_1-1)
    digit_2=(num//pow(10, pos_2-1))%10
    num=num-digit_2*pow(10, pos_2-1)
    #print(digit_1, digit_2, num)
    
    num=num+digit_1*pow(10, pos_2-1)
    num=num+digit_2*pow(10, pos_1-1)
    
    print(num)
    i+=2


















end=time.time()
print("Execution Time : ",end-start)
