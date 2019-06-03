pattern=list(map(str,input().split()))
print(pattern)
number=list(map(int,input().split()))
j=0
for i in range(len(pattern)):
    if pattern[i]=='-':
        print(" ")
        print(number[j])
        j+=1
    else:
        print(number[j])
        j+=1
        