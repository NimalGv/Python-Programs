def bob_remove(lucky_no_bob):
    bob=0
    for i in li:
        if i%lucky_no_bob==0:
            li.remove(i)
            bob=1
    if(bob==1):
        return True
    else:
        return False

def alice_remove(lucky_no_alice):
    alice=0
    for i in li:
        if i%lucky_no_alice==0:
            li.remove(i)
            alice=1
    if(alice==1):
        return True
    else:
        return False


testcase=int(input())
li=[]
while(testcase):
    N,lucky_no_bob,lucky_no_alice=map(int,input().split())
    li=list(map(int,input().split()))
    if bob_remove(lucky_no_bob):
        if alice_remove(lucky_no_alice):
            print("ALICE")
        else:
            print("BOB")
    else:
        print("ALICE")        
    li.clear()
    testcase-=1
    
            
    