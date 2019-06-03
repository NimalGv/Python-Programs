arr=[]
brr=[]
crr=[]
c=0
first=True
sequence_started=False
n=int(input())
for i in range(n):
    arr.append(int(input()))
brr=arr.copy()
brr.sort()
for i in range(1,len(brr)):
    v = brr[c]
    if v+1==brr[i]:
        if first==True:
            crr.append(v)
            crr.append(brr[i])
            first=False
        else:
            crr.append(brr[i])
        c+=1
        sequence_started=True
    elif sequence_started==False:
        c+=1
        continue
    elif sequence_started==True:
        break
for i in range(len(arr)):
    for j in range(len(crr)):
        if arr[i]==crr[j]:
            print(arr[i])