# -*- coding: utf-8 -*-
"""
Given an array arr[], the task is to make all the array elements equal with the given operation. In a single operation, any element of the array can be either multiplied by 2 or by 3. If its possible to make all the array elements equal with the given operation then print Yes else print No. Explanation: Input: arr[] = {50, 75, 100} Output: Yes {50 * 2 * 3, 75 * 2 * 2, 100 * 3} = {300, 300, 300}
"""
def check(l):
    c=[]
    m=[2,3]
    for i in m:
        for j in l:
            if '.0' in str(maximum*i / j):
                c.append(1)
            if equal(c,l):
                return True
    return False
                
        
def equal(c,l):
    if len(l)==c.count(1):
        return True
    else:
        return False
        



li=list(map(int,input().split()))
maximum=max(li)
li.remove(maximum)
if check(li):
    print("Yes")
else:
    print("No")
