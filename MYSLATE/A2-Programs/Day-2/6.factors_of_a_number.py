# -*- coding: utf-8 -*-
"""
printing factors of a number
"""
import time
import math
start=time.time()

#optimizing by checking it is a prime or not
def is_prime(number):
    for i in range(3,int(math.sqrt(number))+1):
        if(number%i==0):
            return False
    return True
    
number=int(input())
number*=2
i=2
while(number!=1):
#    if number%i==0:
#       print(i, end=" ");
    while(number%i==0):
        print(i, end=" ")
        number//=i
    if(is_prime(number)):
        print(number)
        break
    i+=1;
    
    
end=time.time()
print("\n",end-start)