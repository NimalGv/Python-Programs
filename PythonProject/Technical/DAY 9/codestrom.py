
def removedup(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
def add(a,b):
    l1=[]
    for i in range(b+1):
        l1.append(a+i)
    return l1

def sub(a,b):
    l1=[]
    for i in range(b+1):
        l1.append(a-i)   
    return l1

def com(a,b,c):
    l=[]
    for i in range(0,3):
        l.extend(add(a,b))
        l.extend(sub(a,b))
        l.extend(add(a,b))
        l.extend(sub(a,b))
    return l
   
a=[5,8,9]
c=[1,1,1]
b=[2,3,5]
l1=[]
imp=1
count=0
for i in range(0,len(a)):
    l1.extend(removedup(com(a[i],b[i],c[i])))  
    if(imp==1):
        imp_val=len(l1)
        imp+=1
for i in range(imp_val):
    if l1.count(l1[i])==len(a):
        count+=1
print(count)