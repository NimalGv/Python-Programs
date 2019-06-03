# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:18:32 2019

@author: admin
"""
import time
start=time.time()

heap=[5, 15, 10, 55, 25, 1, 3]
   #  0   1   2   3   4  5  6
size=len(heap)
size-=1
pos=size
   
def max_heapify(parent):
    left=parent*2+1
    right=parent*2+2
    if(left > pos):  # NO CHILD , BASE CASE
        return
    if(left==pos):   # ONE CHILD
        if(heap[left]>heap[parent]):
            heap[left], heap[parent]=heap[parent], heap[left]
            return
    if(heap[parent]>heap[left] and heap[parent]>heap[right]):  # TWO CHILDS
        return
    if(heap[left]>heap[right]):
        heap[left], heap[parent]=heap[parent], heap[parent]
        max_heapify(left)
        return
    else:
        heap[right], heap[parent]=heap[parent], heap[right]
        max_heapify(right)
        return
        
def heap_sort():
    global pos
    while(pos>=0):
        for parent in range((pos-1)//2,-1,-1):
            max_heapify(parent)
        pos-=1
    return heap



print(heap_sort())   



end=time.time()
print("\nExecution Time : ",end-start)
