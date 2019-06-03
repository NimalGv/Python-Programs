# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 20:54:07 2019

@author: admin
"""
import time
start=time.time()


number=int(input())
length=len(str(number))


while(number):
    ans=0
    i=0
    temp_2=number
    while(number):
        digit=number%10
        if(digit>0):
            ans=ans+pow(10,i)
        i+=1
        number//=10
    f_ans=str(ans)
    print(f_ans.zfill(length))
    number=temp_2
    number-=ans
        


end=time.time()
print("\nExecution Time : ",end-start)
