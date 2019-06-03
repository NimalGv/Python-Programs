# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:57:15 2019

@author: admin
"""
import time
start=time.time()


read="1"
write=""


for i in range(10):
    index=0
    count=0
    point=read[0]
    while(True):
        
        while(index < len(read)):
            print(len(read),index)
            if(point==read[index]):
                print(index,read[index])
                count+=1
                index+=1
        write+=str(count)
        write+=point
        if(index!=len(read)):
            point=read[index]
            count=0
        else:
            break
    print(write)
    read=write
    write=""
    
    
    
    



end=time.time()
print("\nExecution Time : ",end-start)
