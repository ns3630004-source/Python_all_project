line="-"

print("+,-,*,**,%,/,//,exit")

#--------------------------------------------------------------

while True:

    choice=input("enter your operator given below")

    if choice in ["+","-","*","**","%","/","//","exit"]:

        num1=int(input("enter your first number: "))

        num2=int(input("enter your first number: "))

        print(line*50)
#--------------------------------------------------------------
    if choice=="+":

        print(num1+num2)

        print(line*50)

#--------------------------------------------------------------
   
    elif choice =="-":

        print(num1-num2)

        print(line*50)

#--------------------------------------------------------------

    elif choice=="*":

        print(num1*num2)

        print(line*50)

#--------------------------------------------------------------

    elif choice=="**":

        print(num1**num2)

        print(line*50)

#--------------------------------------------------------------

    elif choice=="/":

        if num2==0:

            print("error not divisble by 0 :")

        else: 

            print(num1/num2)

            print(line*50)

#--------------------------------------------------------------

    elif choice=="//":

        if num2==0:

            print("error not divisble by 0 :")

        else:
            print(num1//num2)
            print(line*50)

#--------------------------------------------------------------

    elif choice=="%":

        if num2==0:

            print("error not divisible by 0: ")

        else:

            print(num1%num2)

            print(line*50)

#--------------------------------------------------------------

    elif choice =="exit":

        print("thanks for using this project:  ")

        break

#--------------------------------------------------------------

    else:

        print("choose please a valid operator: ")