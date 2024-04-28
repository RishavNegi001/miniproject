#NUMBER SYSTEM
n=int(input("enter value till u want to print"))
print("1 for forward and 0 for reverse")
c=int(input("enter c:"))
if(c==1):
    print("2 for vertical and 3 for horizontal")
    d=int(input("enter d:"))
    if(d==2):
        for i in range(1,n+1,1):
            print(i)
    elif(d==3):
        for i in range(1,n+1,1):
            print(i,end=',')
    else:
        print("invalid choice")
elif(c==0):
    print("2 for vertical and 3 for horizontal")
    d=int(input("enter d:"))
    if(d==2):
        for i in range(n,0,-1):
            print(i)
    elif(d==3):
        for i in range(n,0,-1):
            print(i,end=',')
    else:
        print("invalid choice")
else:
    print("invalid choice")  
