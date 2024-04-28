
#inventory management
l={"apple":80,"banana":60,"gauva":100,"oranges":60,"cheese":60,"butter":50,"milk":50,"curd":25,"bread":35,"biscuits":20,"namkeen":80,"soap":55,"shampoo":350,"sugar":50,"egg":70,"softdrinks":95,"fruitjuice":110}
totalamount=0
print(l)
name=input("enter customer name:")
cardamount=int(input("enter card balance:"))
while True:
    cart=input("items purchased:")
    quantity=int(input("enter the quantity:"))
    s=l[cart]
    a=quantity*s
    print(a)
    choice=int(input("1 to continue:"))
    totalamount+=a
    if(choice==1):
        continue;
    else:
        break;
if(cardamount<totalamount):
    print("insufficient balance")
    r=int(input("0 to recharge"))
    if(r==0):
        k=int(input("enter recharge amount"))
        cardamount+=k
        amountleft=cardamount-totalamount
        print("card balance",amountleft)
    else:
        print("no rechgarge")
elif(cardamount>totalamount):
    amountleft=cardamount-totalamount
    print("card balance",amountleft)
else:
    print()  
