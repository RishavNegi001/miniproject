#guessing number
import random
x=int(input("range till u want"))
while True:
    c=random.randint(1,x)
    n=c
    user=int(input("enter the number user want"))
    if(user==n):
        print("right guess")
        break;
    else:
        print("better luck next time")
    choice=int(input("1 to continue"))
    if(choice==1):
        continue;
    else:
        break; 
