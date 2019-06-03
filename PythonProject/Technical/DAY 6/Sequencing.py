"""" Sequencing numbers in decending order """

a,b,c,d=map(int,input().split())

def cmp_four(a,b,c,d):
    if a>b and a>c and a>d:
        print(str(a),end=" > ")
        cmp_three(b,c,d)
    elif b>c and b>d and b>a:
        print(str(b),end=" > ")
        cmp_three(a,c,d)
    elif c>d and c>b and c>a:
        print(str(c),end=" > ")
        cmp_three(b,a,d)
    else:
        print(str(d),end=" > ")
        cmp_three(b,c,a)
    
def cmp_three(a,b,c):
    if a>b and a>c:
        print(str(a),end=" > ")
        cmp_two(b,c)
        return a
    elif b>c:
        print(str(b),end=" > ")
        cmp_two(a,c)
    else:
        print(str(c),end=" > ")
        cmp_two(b,a)
        
def cmp_two(a,b):
    if a>b:
        print(str(a),end=" > ")
        print(str(b))
    else:
        print(str(b),end=" > ")
        print(str(a))

cmp_four(a,b,c,d)