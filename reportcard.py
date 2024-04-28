#report card
with open('user_input.txt', 'w') as file:
    name = input("Enter your name: ")
    uni_roll= input("Enter your university roll no.: ")

    marks=int(input("Enter total marks of 5 Subject"))
    res=(marks*100)/500
    file.write(f"Name: {name}\n")
    file.write(f"University roll no.: {uni_roll}\n")
    if res<=40:
        file.write(f"Result:{"Fail"}\n")
    else:
        file.write(f"Result:{"Pass"}\n")    
with open ('user_input.txt','r') as file:
    print(file.read())



