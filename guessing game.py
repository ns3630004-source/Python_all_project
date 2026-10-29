import random # import random number library method.

line="-"

attempt=0

while True:

   numbers=random.randint(1,10) # number guessing random from 1 to 10

   number=int(input("enter your guessing number:\n"))
   attempt+=1 

 # check the number is equl aur greater than compter choice by user and computer    
 
   if number>numbers:
        print("computer guessing number is: ",numbers)
        print("your number is greater than computer choice number :")
        print("choose a smaller number of compter choice number: ")
        print(line*60)

   elif number<numbers:
        print("computer choice number is :",numbers)
        print("your number is less than computer choice number :")   
        print("choose a longest number of compter choice number : ") 
        print(line*60)

   elif number==numbers:
        print("congratulations you win this number guessing game : ") 
        print(line*60)
        break

# total attempt of user

print("your total attempt is",attempt)    