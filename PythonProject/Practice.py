n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
j=1
for i in range(n):
    if a[i]==a[j]:
        j+=1
    else:
        break
print (a[j])