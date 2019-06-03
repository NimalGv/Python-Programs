a,b,c=map(int,input().split())
if a+b > c :
    if b+c > a :
        if a+c > b:
            print("Can")
        else:
            print("Cannot")
    else:
        print("Cannot")
else:
    print("Cannot")