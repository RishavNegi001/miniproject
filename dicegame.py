#roll the dice

import random
user=0;comp=0
while True:
    c=random.randint(1,7)
    n=c
    comp+=1
    i=int(input("enter the value:"))
    if(1<=i<=6):
        user+=i
    else:
        print("value out of range")
    k=int(input("enter 9 to continue"))
    if(k==9):
        continue;
    else:
        break;
print("user total",user)
print("computer total",comp)
if(user>comp):
    print("win",user)
elif(comp>user):
    print("loss",comp)
else:
    print("its a tie")  
