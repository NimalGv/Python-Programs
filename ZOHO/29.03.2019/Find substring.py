# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 21:53:06 2019

@author: admin
"""
import time
start=time.time()

end_index=[]

def is_left(array, substring, start_index):
    global end_index
    
    length=len(substring)
    index=1
    if(start_index[1]<=len(array[start_index[1]])-len(substring)):
        pass
    else:
        return False
    for j in range(start_index[1]+1, len(array[start_index[0]])):
        if(index<length):
            end_index=[]
            if(substring[index]==array[start_index[0]][j]):
                end_index.append(start_index[0])
                end_index.append(j)
                index+=1
                continue
            else:
                end_index=[]
                return False
    
    return True

def is_down(array, substring, start_index):
    global end_index
    end_index=[]
    length=len(substring)
    index=1
    if(start_index[0]<=len(array)-len(substring)):
        pass
    else:
        return False
    for j in range(start_index[0]+1, len(array)):
        if(index<length):
            end_index=[]
            if(substring[index]==array[j][start_index[1]]):
                end_index.append(j)
                end_index.append(start_index[1])
                index+=1
                continue
            else:
                end_index=[]
                return False
    
    return True

def count_first(array, string):
    count=0
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            if(array[i][j]==string):
                 count+=1
    return count
            
def find_first_i(array, string, count):
    index=0
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            if(array[i][j]==string):
                index+=1
                if(count==index):
                    return i

def find_first_j(array, string, count):
    index=0
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            if(array[i][j]==string):
                index+=1
                if(count==index):
                    return j

array=[['W','E','L','C','O'],
       ['M','E','T','O','O'],
       ['O','H','C','C','O'],
       ['R','P','O','R','A'],
       ['T','I','O','A']]

substring="CO"

start_index=[]
count=count_first(array, substring[0])

for i in range(1, count+1):
    start_index.append(find_first_i(array, substring[0], i))
    start_index.append(find_first_j(array, substring[0], i))
   # print(start_index)
   # print(count)
    if(is_left(array, substring, start_index)):
        print(start_index, end=" ")
        print(end_index)
    if(is_down(array, substring, start_index)):
        print(start_index, end=" ")
        print(end_index)
    start_index=[]




end=time.time()
print("\nExecution Time : ",end-start)
