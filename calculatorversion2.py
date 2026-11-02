
print("+,-,*,/,//,%,**,exit")

while True:

    choice=input("enter your operator given below: ")

    if choice in ["+","-","*","**","/","//","%"]:

        number1=int(input("enter your first number: "))

        number2=int(input("enter your second number :"))
    else:
        print("thanks for using sir/madam :")
        break


    match choice:

        case "+":

            print(number1+number2)

        case "-":

            print(number1-number2)

        case "*":

            print(number1*number2)

        case "/":

            print(number1/number2)

        case "//" :

            print(number1//number2)

        case "%" :

            print(number1%number2)

        case _ :

            print("choose a valid operator given below: ")