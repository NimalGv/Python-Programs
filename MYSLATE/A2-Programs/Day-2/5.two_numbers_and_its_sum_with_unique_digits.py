# -*- coding: utf-8 -*-
"""
Two numbers and its sum must be of unique digits
    eg: abc + def = ghij
    
    combine all numbers -> abcdefghij
    check if all numbers had occured only once -> # use array to maintain a counter
                                                  # use 9876543210 -> 0 is in 10^0 position.
                                                                      2 is in 10^2 position.
                                                                      5 is in 10^5 position.
                                                                      9 is in 10^9 position.
    number * 10^number
    
    so if all digit occurs it should be equal to 987654321                                                                   
"""

def all_occured_tens_pos(number):
    str_no=str(number)
    no=0
    for i in str_no:
        no+=int(i)*pow(10,int(i))
    #print("All Occured : ",no)
    if(no==9876543210):
        return True
    else:
        return False

def all_occured_binary(number):
    str_no=str(number)
    no=0
    for i in str_no:
        no+=pow(2,int(i))
    #print("All Occured : ",no)
    if(no==1023):
        return True
    else:
        return False 

    
    
#print(all_occured(2467891035))  
        
start,end=map(int, input().split())
for i in range(start,end+1):
    for j in range(start, end+1):
        if(i+j > 999):
            combined_no=(i*1000)+j
            combined_no=(combined_no*10000)+(i+j)
            if(all_occured_binary(combined_no)):
                print(i, "+", j, "=", i+j)
               # print("CO-No:", combined_no, end=":")

                                                                
                                                                      
                                                            
                                                                    

