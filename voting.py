
count1=0 # yha ye global variable hain

line="-"

def bjb():

   
    global count1 # value ko increment krne ke liye global use kiya hoon agr shirf read mtlb dekhna hota to global use krta.

   
    count1+=1



count2=0

def sapa():

    global count2


    count2+=1



count3=0

def kangress():

    global count3

    
    count3+=1





while True:

    print("0 for exit ")

    print(line*50)

    print("1 for BJp")

    print(line*50)
    
    print("2 for Sapa")

    print(line*50)
    
    print("3 for Kangress")

    print(line*50)
    

    choice=int(input("enter your choice: "))

    match choice:

        case 0:

            if count1>count2 and count1>count3:

                print("bjp wins",count1)
                print(line*50)
                

            elif count2>count3 and count2>count3:

                print("sapa wins: ",count2)
                print(line*50)
                

            else:
                print("kangress wins: ")
                print(line*50)
                

            if choice==0:
                print("thanks for using project sir/madam")
                print(line*50)
                
                break

        case 1:

            bjb()

        case 2:

             sapa()

        case 3:

            kangress()

        case _:

            print("Please choose a valid party: ")
