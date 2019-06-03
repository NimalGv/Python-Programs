# -*- coding: utf-8 -*-
"""
Created on Fri May 31 21:46:55 2019

@author: admin
"""
import time
start=time.time()

from itertools import permutations

p=list(permutations(["ab", "bc"]))

print(p)



end=time.time()
print("\nExecution Time : ",end-start)
