print("1.small-price:200\n2.medium-price:300\n3.large-price:400")
b=int(input("how many pizza do you need="))
a=input("Enter the size of pizza=").lower()
e=0
f=0
try:
    if(a!="small" or a!="medium" or a!="large" ):
        print("Please enter in chocies from the above options ")

    if(a=="small"):
        pizza=b*200
        c=input("Enter that do you need to add  pizza toppings(yes or no)=").lower()
        d=input("Enter that do you need to add cheese pizza (yes or no)=").lower()
        if(c=="yes" and d=="yes"):
            e=pizza*5/100
            f=b*20
        elif(c=="yes" and d=="no"):
            e=pizza*5/100
        elif(c=="no" and d=="yes"):
            f=b*20
        else:
            print("you have not add toppings and cheese in it")
            
            
    elif(a=="medium"):
        pizza=b*300
        c=input("Enter that do you need to add  pizza toppings(yes or no)=").lower()
        d=input("Enter that do you need to add cheese pizza (yes or no)=").lower()
        if(c=="yes" and d=="yes"):
            e=pizza*5/100
            f=b*20
        elif(c=="yes" and d=="no"):
            e=pizza*5/100
        elif(c=="no" and d=="yes"):
            f=b*30
        else:
            print("you have not add toppings and cheese in it")
    elif(a=="large"):
        pizza=b*400
        c=input("Enter that do you need to add  pizza toppings(yes or no)=").lower()
        d=input("Enter that do you need to add cheese pizza (yes or no)=").lower()
        if(c=="yes" and d=="yes"):
            e=pizza*5/100
            f=b*20
        elif(c=="yes" and d=="no"):
            e=pizza*5/100
        elif(c=="no" and d=="yes"):
            f=b*40
        else:
            print("you have not add toppings and cheese in it")
    

    total=pizza+e+f
    Pi=str(pizza)
    E=str(e)
    F=str(f)
    Total=str(total)
    print("╔══════════════════════╦════════════╗")
    print(f"║ Amount of PIZZA only ║    {Pi}{' '*(6-(len(Pi)))}  ║")
    print("║══════════════════════╬════════════║")
    print(f"║ ADDED toppings       ║    {E}{' '*(6-(len(E)))}  ║")
    print("║══════════════════════╬════════════║")
    print(f"║ ADDED cheese         ║    {F}{' '*(6-(len(F)))}  ║")
    print("║══════════════════════╬════════════║")
    print(f"║ Total                ║   {Total}{' '*(6-(len(Total)))}   ║")
    print("╚══════════════════════╩════════════╝")

finally:
    print("The program is completed.....")

