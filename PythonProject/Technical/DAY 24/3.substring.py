# -*- coding: utf-8 -*-
"""
Kiran has been a given a problem by his brother Narik .The problem is related to strings. Now he gives Kiran a long String S which consists of lowercase English Alphabets and wants him to tell the minimum size of substring such that all the substrings of that size in S have at least K Consonants(Non-vowels) in them. If none of the subArray size satisfy the above condition ,return -1.
"""

li1=[]
def substring(str):
    for i in range(len(str)):
        li1.append(str[i:])
        substring(str[i:i-1])
    return li1

def constantcount(string):
    count=0
    for i in string:
        if i !='a' and i !='e' and i !='i' and i !='o' and i !='u':
            count+=1
    if count>=k:
        li3.append(len(string))
        
string=input()
k=int(input())
li2=substring(string)
li3=[]
for i in li2:
    constantcount(i)
li4=[]
for i in li3:
    if i not in li4:
        li4.append(i)
li5=[]
for i in li4:
    li5.append(li3.count(i))
valuemax=max(li5)
li6=[]
for i in li4:
    if li3.count(i)==valuemax:
        li6.append(i)
li6.sort(reverse=True)
if len(li6)!=0:
    print(li6[0])
else:
    print('-1')
    