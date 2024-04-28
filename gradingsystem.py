#grading system
f=open('record file','w')
while True:
    name=input("enter the student name:")
    marks=int(input("enter student total marks:"))
    k=500
    p=(marks/k)*100
    if(95<=p<=100):
        print("student got A+ grade",p)
    elif(90<=p<95):
         print("student got A grade",p)
    elif(80<=p<90):
         print("student got B grade",p)
    elif(70<=p<80):
         print("student got C grade",p)
    elif(60<=p<70):
         print("student got D grade",p)
    elif(0<=p<60):
         print("student got F grade",p)
    else:
        print("H")
    f.write("name:-(name)percentage:-(p)")
    choice=int(input("1 to continue "))
    if(choice==1):
        continue;
    else:
        break;   
