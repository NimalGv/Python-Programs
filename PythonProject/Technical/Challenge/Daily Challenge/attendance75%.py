# -*- coding: utf-8 -*-
"""
Consider the subject Data Structures for which a total number of classes held till present date is M and some students attend only N out of these classes. Find the minimum number of lectures they have to attend so that their 75% attendance is maintained. Note :- Input : M = 9 and N = 1 Output : 23 lectures to attend Out of 9 classes only 1 class is attended. After 23 more classes a total of 1+23 = 24 classes have been attended and total number of classes held = 9+23 = 32. So 24/32 = 75%. Hence 23 is the minimum value.
"""
import math


m=int(input())
n=int(input())
if n<math.ceil(0.75*m):
    print(math.ceil(((0.75*m)-n)/0.25))
else:
    print("0")
    
    
    
    
    '''
      (0.75*M)-N
      ----------
         0.25    '''   