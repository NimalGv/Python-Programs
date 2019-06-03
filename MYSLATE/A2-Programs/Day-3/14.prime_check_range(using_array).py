# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:59:08 2019

@author: admin

Execution Time :  173.88703441619873
Execution Time :  67.78999161720276 (leaving evens) faster than the above
Execution Time :  78.52060747146606 (Using list or arrays) much faster than others in c

"""
import time
import math
start=time.time()


limit=10000000
count=1
li=[]
li.append(2)
for i in range(3,limit+1,+2):
    j=0
    till=int(math.sqrt(i))
    while(li[j]<=till):
       if(i%li[j]==0):
           break
       j+=1
    if(li[j]>till):
        li.append(i)
        count+=1
print(count)


end=time.time()
print("\nExecution Time : ",end-start)
