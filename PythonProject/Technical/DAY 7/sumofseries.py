
"""
Sum of the series 1 + (1+3) + (1+3+5) + (1+3+5+7) + …… + (1+3+5+7+…+(2n-1))
"""

def series(n):
    if n == 1:
        return 1
    sum=0
    for i in range(1,n+1,2):
        sum+=i
    return sum+series(n-2)

n=int(input())
print(series(2*n-1))