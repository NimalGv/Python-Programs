# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 21:09:32 2019

@author: admin
"""
import time
start=time.time()

## works on all size of matrices

def rotate_array_90(array1, row, col):
    #90' rotation
    left1=[[0 for i in range(row)] for j in range(col)] 
    for i in range(0, row):
        for j in range(0, col):
            left1[j][row-i-1]=array1[i][j]
    print_array(left1)
    return left1
    

def print_array(array):
    for i in array:
        print(*i)
    print()
    
## works on square matrix only
    
def is_90(array1, row, col, array2):
    for i in range(0, row):
        for j in range(0, col):
            if array2[j][col-i-1]!=array1[i][j]:
                return False
    return True
    
def is_180(array1, row, col, array2):
    for i in range(0, row):
        for j in range(0, col):
            if array2[row-i-1][col-1-j]!=array1[i][j]:
                return False
    return True    

def is_270(array1, row, col, array2):
    for i in range(0, row):
        for j in range(0, col):
            if array2[col-1-j][i]!=array1[i][j]:
                return False
    return True   

def is_360(array1, row, col, array2):
    for i in range(0, row):
        for j in range(0, col):
            if array2[i][j]!=array1[i][j]:
                return False
    return True   
    
array=[[1,2,3],[4,5,6],[7,8,9]]
array2=[[7, 4, 1],[8, 5, 2],[9, 6, 3]]

row=len(array)
col=len(array[0])

print_array(array)
rotate_array_90(rotate_array_90(rotate_array_90(rotate_array_90(array, row, col),col,row),row,col),col,row)

print(is_90(array, col, row, array2))
print(is_180(array, row, col, array2))
print(is_270(array, row, col, array2))
print(is_360(array, row, col, array2))


end=time.time()
print("\nExecution Time : ",end-start)
