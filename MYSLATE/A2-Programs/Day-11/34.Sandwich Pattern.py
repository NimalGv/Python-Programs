# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 22:49:04 2019

@author: admin
"""
import time
start=time.time()


num=11
printno=1
if(num%2==0):
    limit=num//2-1
    even=True
else:
    limit=num//2
    even=False
    
if(even):
    for i in range(0, limit+1):
        for j in range(0, num):
            s=str(printno)
            print(s.zfill(3), end=" ")
            printno+=1
        printno+=num
        print()
    printno-=num
    for i in range(0, num):
        s=str(printno)
        print(s.zfill(3), end=" ")
        printno+=1
    print()
    printno-=1
    for i in range(0, num-limit-2):
        printno=printno-(num*2)-num+1
        for j in range(0, num):
            s=str(printno)
            print(s.zfill(3), end=" ")
            printno+=1
        print()
        printno-=1
else:
    for i in range(0, limit+1):
        for j in range(0, num):
            s=str(printno)
            print(s.zfill(3), end=" ")
            printno+=1
        printno+=num
        print()
    printno-=num+1
    printno=printno-(num*1)-num+1
    for i in range(0, num):
        s=str(printno)
        print(s.zfill(3), end=" ")
        printno+=1
    print()
    printno-=1
    for i in range(2, num-limit):
        printno=printno-(num*2)-num+1
        for j in range(0, num):
            s=str(printno)
            print(s.zfill(3), end=" ")
            printno+=1
        print()
        printno-=1
    
            
        


end=time.time()
print("\nExecution Time : ",end-start)
4