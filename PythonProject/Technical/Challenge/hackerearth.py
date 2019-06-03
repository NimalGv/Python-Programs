# -*- coding: utf-8 -*-
"""

"""
test=int(input())
while(test):
    str1=input()
    str2=input()
    li=[]
    for i in str1:
        li.append(i)
    count=0
    for i in range(len(li)):
        s=li[i]
        li.pop(i)
        string=''.join(li)
        if str2 in string:
            count+=1
        del string
        li.insert(i,s)
    if count:
        print("Yes")
        print(count)
    else:
        print("No")
    test-=1