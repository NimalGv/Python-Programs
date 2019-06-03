# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:10:22 2019

@author: admin
"""
import time
start=time.time()

#range 0-999

ones=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens=["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
number=316
safe=number
digit=[]

for i in range(len(str(number))-1, -1, -1):
    digit.append(number//(10**i))
    number%=(10**i)
number=safe
index=0
print(digit)
for i in range(len(str(number))-1, -1, -1):
    if(i==2):
        print(ones[digit[index]],"hundred and",end=" ")
    if(i==1):
        if(digit[index]==1):
            if(digit[index+1]==0):
                print(tens[0],end=" ")
                break
        if(digit[index]==1):
                print(ones[digit[index]*10+digit[index+1]-1])
                break
        else:
            print(tens[digit[index]-1], end=" ")
    if(i==0):
        print(ones[digit[index]])
    #print(digit)
    number%=(10**i)
    index+=1
    

end=time.time()
print("\nExecution Time : ",end-start)
