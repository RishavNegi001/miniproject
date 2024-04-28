#voting system
b=0;c=0;a=0;s=0;r=0
while True:
    name=input("enter your name:")
    n=int(input("enter your age:"))
    if(n>=18):
        print("eligble to vote")
        print("bjp==1;INC==2;AAP==3;BSP==4;RLD==5")
        p=int(input("enter the party u want to vote"))
        if(p==1):
            b+=1
            print("BJP total votes:",b)
        elif(p==2):
            c+=1
            print("INC total votes:",c)
        elif(p==3):
            a+=1
            print("AAP total votes:",a)
        elif(p==4):
            s+=1
            print("BSP total votes:",s)
        elif(p==5):
            r+=1
            print("RLD total votes:",r)
        else:
            print("invalid")
        ch=int(input("press 10 to continue:"))
        if(ch==10):
            continue;
        else:
            break;
    else:
        print("no eligble to vote")
print("voting is ended")    
    
        


