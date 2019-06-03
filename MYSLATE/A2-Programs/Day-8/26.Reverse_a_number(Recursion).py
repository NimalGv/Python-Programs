# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:19:49 2019

@author: admin
"""
import time
start=time.time()



def reverse(number, power):
    if(number==0):
        return 0
    return number%10*(10**power)+reverse(number//10, power-1)

number=132124124534635364544542570001
print(reverse(number, len(str(number))-1))

end=time.time()
print("\nExecution Time : ",end-start)
