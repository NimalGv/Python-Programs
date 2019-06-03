# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:20:32 2019

@author: admin
"""
import time
start=time.time()


num=9
printno=1
no=num*num+1
sa=no
for i in range(num, -1, -1):
    if i!=num:
        no=sa-i
        sa=no
    for space in range(num-i, 0, -1):
        print("   ",end="")
    for j in range(0, i):
        s=str(printno)
        print(s.zfill(2), end=" ")
        printno+=1
    printno-=1
    for j in range(0, i):
        s=str(no)
        print(s.zfill(2), end=" ")
        no+=1
    printno+=1
    print()
    
        


end=time.time()
print("\nExecution Time : ",end-start)
