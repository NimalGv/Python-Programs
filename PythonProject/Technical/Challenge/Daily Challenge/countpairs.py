# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:35:08 2019

@author: admin
"""
def checkpair(a,b):
    a=str(a)
    b=str(b)
    for i in range(len(a)) :  
        for j in range(len(b)) :  
            if (a[i] == b[j]) : 
                return True; 
    return False;  

def pairGen(array):
    count=0
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
           # print(array[i],",",array[j],end="=")
            if checkpair(array[i],array[j]):
                count+=1
    return count
            
li=list(map(int,input().split()))
li.sort()
print(pairGen(li))
