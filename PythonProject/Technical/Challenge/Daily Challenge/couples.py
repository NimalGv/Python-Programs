# -*- coding: utf-8 -*-
"""
To celebrate the anniversary of Googleland, N couples are going to go for a boat ride in a rowboat. The rowboat is very long, but it is only one person wide, so the people will sit in a line from front to back. However, during a rehearsal of the voyage, the boat did not move! After investigating, the organizers found that some newlywed couples were not rowing, but writing love poems for each other the whole time. Specifically, there are M pairs of newlywed couples. If the two members of a newlywed couple are sitting next to each other, they will be so busy writing poems that they will not row. Now the organizers have come to you, the smartest person in Googleland, to ask, how many possible ways are there to arrange all 2N people on the rowboat, such that for each of the M newlywed couples, the two members are not sitting next to each other? Two ways are different if there is some position in the boat at which the two ways use different people. Notice that for the purpose of counting the number of ways, the two members of a couple are not considered to be interchangeable. Since the number can be very large, the organizers only want to know the value of the answer modulo 1000000007(109+7).
"""
from itertools import permutations
import itertools
N,M=map(int,input().split())
li1=[]
li2=[]
count=0
caps=65
for i in range(N-M):
    a=chr(caps)
    li1.append(a)
    li1.append(a)
    caps+=1
li3=[]
small=97
for i in range(M):
    a=chr(small)
    li1.append(a)
    li1.append(a)
    li3.append(a+a)
    small+=1
li2=list(permutations(li1,N*2))
for i in li2:
    v=''.join(itertools.chain(*i))
    for i in li3:
        if i not in v:
            count+=1
print(count)
