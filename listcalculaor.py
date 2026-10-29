
print("+ ,-,/,//,**,%")

choice=input("please choose a operator given below : ")

if choice in ["+","-","/","//","%","*"]:
  value1=int(input("enter your first number:"))
  value2=int(input("enter your second number: "))

if choice=="+":
    print(value1+value2)

elif choice=="-":
   print(value1-value2) 

elif choice=="/":
    
    if value2==0:
      print("not divisible by 0: ")

    else:
      print(value1/value2)

elif choice=="//":
    
    if value2==0:
      print("not divisible 0: ")
    else:
      print(value1//value2)

elif choice=="%":
    
    if value2==0:
       print("not divisible by 0 : ") 

    else:
     print(value1%value2)
     
else:
   print("please choose a valid opertor: ")     
      