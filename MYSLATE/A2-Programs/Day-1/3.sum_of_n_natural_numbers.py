# -*- coding: utf-8 -*-
"""
sum of "n":
            sum of odd        +        sum of even;

        n=range-no_of_even               n=range/2

               n*n            +           n*(n+1)

               thus -> sum of "n" numbers
               
               Further reducing above gives -> n*(n+1)/2
"""
limit=int(input())
no_of_even=limit//2
no_of_odd=limit-no_of_even
print("1.Sum of 'n' numbers : ", (no_of_even*(no_of_even+1))+(no_of_odd*no_of_odd))
print("2.Sum of 'n' numbers : ", limit*(limit+1)//2)

