# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:19:13 2019

@author: admin
"""
import time
start=time.time()


number=32986
one=False
two=False
no=False
while(number):
    if(number&1):
        if(not one):
            one=True
            two=False
            print(1)
        else:
            print("=",1)
            no=True
            break
    else:
        if(not two):
            two=True
            one=False
            print(0)
        else:
            print("=",0)
            no=True
            break
    number=number>>1

if(no):
    print("No")
else:
    print("Yes")

end=time.time()
print("\nExecution Time : ",end-start)
