# square function.

def square():

    number=int(input("enter your number: "))

    print(number*number)
    print(line*30)

#-------------------------------------------------    

#positive negative.

def positivenegative():

    number=int(input("enter your value: "))

    print("positive") if number>0  else print("negative")
    print(line*30)

#------------------------------------------------- 

# factorial number.

def factorial():

    f=1

    number=int(input("enter your ending number of loop :"))

    for i in range(1,number+1):

        f=f*i

    print("your total factorial number is :",f)

    print(line*30)

#------------------------------------------------- 

# even odd.

def evenodd():

    number=int(input("enter your even odd number: "))

    print("even number") if number%2==0 else print("odd number:")

    print(line*30)


#------------------------------------------------- 

# simple table.

def table():

    number=int(input("enter your table number: "))

    for i in range(1,11):

        print(number*i)
        
    print(line*30)

#------------------------------------------------- 

# super table.

def supertable():

    number=int(input("enter your table number: "))

    for i in range(1,11):

        print(number,"*",i,"=",number*i) 

    print(line*30)

#------------------------------------------------- 

#  list.

my_list=[]

def mylist():

    number=int(input("enter your ending number to stop loop: "))

    for i in range(1,number+1):

        fruits=input("enter your fruits name: ")
        my_list.append(fruits)

    print(my_list)


#------------------------------------------------- 

# list sort method.

def assending():

    my_list.sort()

    print(my_list)

    print(line*60)

#------------------------------------------------- 

# list reverse methods.

def decending():

    my_list.sort(reverse=True)
    print(my_list)

    print(line*60)
    


#------------------------------------------------- 

# list insert method.

def insert():

    fruit=input("enter your new fruit name adding any index: ")

    num=int(input("enter your index number to add fruit: "))

    my_list.insert(num,fruit)

    print(my_list)

    print(line*60)
    

#------------------------------------------------- 

# list pop method.

def pop():

    my_list.pop()
    print(my_list)

    print(line*60)


#------------------------------------------------- 

# list reverse.

def reverse():

    my_list.reverse()
    print(my_list)

    print(line*30)


#------------------------------------------------- 

# tuple.



my=()
    

def adding():
     
    t=list(my) 

    num=int(input("enter your number to stop loop."))

    for i in range(1,num+1):

        num2=int(input("enter your adding  number into a tuple: "))

        t.append(num2)

    t=tuple(t)

    print(t)

    print(line*60)

#------------------------------------------------- 

# set .

my_set=set()

def add():

    num=int(input("enter your number to stop loop."))

    for i in range(1,num+1):

        num2=int(input("enter your number to add in a set ."))

        my_set.add(num2)

    print(my_set)

    print(line*35)

#------------------------------------------------- 

# dictionary.

my_dict={ 


}

def insert():

    num=int(input("enter your number to stop loop."))

    for i in range(1,num+1):

       name=input("enter your name:")
       Course=input("enter your course: ")

       my_dict.update({name:Course})

    print(my_dict)

    print(line*60)

   

#------------------------------------------------- 

# dict keys.

def keys():

    print(my_dict.keys())

    print(line*60)

#------------------------------------------------- 

# dict values.

def value():

    print(my_dict.values())

    print(line*60)

#-------------------------------------------------

# print statement on the compiler
line="-"

print("0 for exit. ")
print(line*30)

#-------------------------------------------------

print("1 for square .")
print(line*30)

#-------------------------------------------------

print("2 for positive negative .")
print(line*30)

#-------------------------------------------------

print("3 for factorial .")
print(line*30)

#-------------------------------------------------'

print("4 for evenodd .")
print(line*30)

#-------------------------------------------------

print("5 for table .")
print(line*30)

#-------------------------------------------------

print("6 for supertable .")
print(line*30)

#-------------------------------------------------

print("7 for my list .")
print(line*30)

#-------------------------------------------------

print("8 for check assending number into a list .")
print(line*30)

#-------------------------------------------------

print("9 for check for decending number into a list .")
print(line*30)

#-------------------------------------------------

print("10 for insert any  number into a list index .")
print(line*30)

#-------------------------------------------------

print("11 for random delete number into a list .")
print(line*30)

#-------------------------------------------------

print("12 for list reverse .")
print(line*30)

#-------------------------------------------------

print("13 for adding a number into a tuple .")
print(line*30)

#-------------------------------------------------

print("14 for adding number into a set .")
print(line*35)

#-------------------------------------------------

print("15 for adding name and course into dictionary.")
print(line*60)

#-------------------------------------------------

print("16 for check keys in dictionary .")
print(line*60)

#-------------------------------------------------

print("17 for check for values in dictionary.")
print(line*60)

#-------------------------------------------------


# fundtionc calling .

while True:

  choice=int(input("enter your number: "))

  match choice:

    case 0:
          if choice==0:
              print("Thankyou sir / madam using this project : ")
              break

    case 1:

        square()

    case 2:

        positivenegative()

    case 3:

        factorial()

    case 4:

        evenodd()

    case 5:

        table()

    case 6:

        supertable()

    case 7:

        mylist()

    case 8:

        assending()

    case 9:

     decending()

    case 10:

        insert()

    case 11:

        pop()

    case 12:

        reverse()

    case 13:

        adding()

    case 14:

        add()

    case 15:

        insert()

    case 16:

        keys()

    case 17:


        value()

    case _ :

        print("choose a valid number given below")
        