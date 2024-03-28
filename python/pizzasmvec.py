print("\t\t\t\tWecome to JUNGLE PIZZA \n\n")
print("TODAY OFFER :\n if you purchase above thousand(1000) you would get 20% of discount\n if you purchase above five hundred(500) you would get 10% of discount")
print(" TODAY'S SPEtCIAL VARIETY's PIZZA AVALIBLE  :\n\t 1.MARGHERITA PIZZA\n\t 2.CHICKEN PIZZA\n\t 3.CORN PIZZA\n\t 4.PANNER PIZZA\n")
p=input("What pizza do you need:").lower()
if(p=="margherita pizza" or p=="chicken pizza" or p=="corn pizza" or p=="panner pizza"):
    print("1.small-price:200\n2.medium-price:300\n3.large-price:400")
    a=input("Enter the size of pizza=").lower()
    b=int(input("how many pizza do you need="))
    e=0
    f=0
    if(a=="small"):
        pizza=b*200 
        if(pizza>=1000):
            e=pizza*20/100
            f=int(pizza-e)
            print(f"Total amount of pizza {pizza}")
            print(f"you  have 20% discount, your total amount is {f} only")
        elif(pizza>=500 and pizza<=1000 ):
            e=pizza*10/100
            f=int(pizza-e)
            print(f"Total amount of pizza {pizza}")
            print(f"you  have 10% discount, your total amount is {f} only")
        else:
            print(f"you dont have discount and total amount is {pizza}only")
             
    elif(a=="medium"):
        pizza=b*300
        if(pizza>=1000):
            e=pizza*20/100
            f=int(pizza-e)
            print(f"Total amount of pizza {pizza}")
            print(f"you  have 20% discount, your total amount is {f} only")
        elif(pizza>=500 and pizza<=1000):
            f=int(pizza-e)
            print(f"Total amount of pizza {pizza}")
            print(f"you  have 10% discount, your total amount is {f} only")
        else:
            print(f"you dont have discount and total amount is {pizza}only")
            
    if(a=="large"):
        pizza=b*400
        if(pizza>=1000):
            e=pizza*20/100
            f=int(pizza-e)
            print(f"Total amount of pizza {pizza}")
            print(f"you  have 20% discount, your total amount is {f} only")
        elif(pizza>=500 and pizza<=1000 ):
            e=pizza*10/100
            f=int(pizza-e)
            print(f"Total amount of pizza {pizza}")
            print(f"you  have 10% discount, your total amount is {f} only")
        else:
            print(f"you dont have discount and total amount is {pizza} only")
            
else:
    print("Plese, Choose the pizza from the above given choise's ")
    
