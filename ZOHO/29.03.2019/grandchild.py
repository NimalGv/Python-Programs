# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 23:17:20 2019

@author: admin
"""
import time
start=time.time()
count=0

def isFather(name):
    global count
    print(name)
    for i in family:
        if name in i[1]:
            count+=1
            isFather(i[0])
    return 


family=[["luke", "shaw"],["wayne", "rooney"],["rooney", "ronaldo"], ["shaw", "rooney"]]
isFather("rooney")
print(count)
        

end=time.time()
print("\nExecution Time : ",end-start)
