'''def substrings(string):
   length = len(string)+1
   return [string[x:y] for x in range(length) for y in range(length) if string[x:y]]
'''
def check(s):
    if s2 in s:
        return True
    else:
        return False

def process(li,s):
   l2=li.copy()
   s=''
   count=0
   for i in range(len(li)):
       li[i]='0'
       for j in li:
           if j!='0':
               s+=j
       if check(s):
           count+=1
       li[i]=l2[i]
       s=''
   return count


s=input()
s2=input()
li=[]
for i in s:
    li.append(i)

if process(li,s):
    print("YES")
    print(process(li,s))
else:
    print("NO")