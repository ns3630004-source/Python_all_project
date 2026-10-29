
pin=1234
attempt=0

print("welcome sir and madam  😊😊😊😊😊:" )

# pin verify

for i in range(1,4):

    verify=int(input("enter your pin : \n "))
    attempt+=1

   # pin loigc yha hain

    if pin==verify: 
        print("access ganted: 😊😊 \n")
        print("hello everone")
        print("hello everone")
        break

    else:
        print("wrong password : \n")
        
if attempt==3:
    print("your card is block 5 minutes : ") # pin logic yha pr khatam hain.


#yha se withdrawl aur add ka logic suru hain.

else:

    while True:
     
      # display part main option ke liye hain ye.

     line1="-"
     
     print("1 for adding amount: \n")
     print("2 for withdrawl amount:\n")
     print("3 for check last withdrawl amount: \n")
     print("4 for check total balance in your account: \n")
     print("5 for exit\n")
     print(line1*50)

     choice=int(input("enter your choice \n"))

     match choice:
         
        case 1:

             # adding amount in account logic.

            amount=int(input("enter your amount :\n"))
            a=0
            amount=amount+a
            line2="-"

            print("successfully adding amount in your bank account :\n")
            print("your total balance is :\n",amount)
            print(line2*50)

        case 2:

            # withdrwal amount logic here.

            withdrawl=int(input("enter your withdrawl amount:\n"))

            line3="-"

            if amount >= withdrawl:

                b=amount-withdrawl

                print("successfully withdrawl amount")
                print("your total balance:\n",b)
                print(line3*50)
            else:
                print("infullence balance :\n")
                print(line3*50)

        case 3:

             # check lat withdrawl amount logic is here.

            line4="-"

            last=withdrawl
            print("your last withdrawl amount is: \n",last)
            print(line4*50)

        case 4:

               # total balance logic is here
            line5="-"

            totalbalance=b
            print("your total balance is: \n",totalbalance)
            print(line5*50)

        case 5:

            line6="-"

            if choice==5:
                print("thankyou sir/madam using this atm machine")
                print(line6*50)
                break    

        case _:
            print("invalid case")

        