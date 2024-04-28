#basic calculator
n1=float(input("enter number 1:"))
n2=float(input("enter number 2:"))
choice=input("enter your choice:")
if(choice=="sum"):
    print(n1+n2)
elif(choice=="subtract"):
    print(n1-n2)
elif(choice=="quotient"):
    print(n1/n2)
elif(choice=="reminder"):
    print(n1%n2)
elif(choice=="multiply"):
    print(n1*n2)
else:
    print("invalid choice") 
