# -*- coding: utf-8 -*-
"""
 capitalize first and last letter of each word in the given line.
"""
string=input()
li=string.split()
for i in range(len(li)):
    li[i]=li[i].replace(li[i][0],li[i][0].upper(),1)
    li[i]=li[i].replace(li[i][len(li[i])-1],li[i][len(li[i])-1].upper(),1)

print(*li)