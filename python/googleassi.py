a=input("ENTER A QUESTION :").lower()
g=["mother","father","brother"]
if("google"in a):
    print("HOW CAN I HELP YOU ?")
    b=input("").lower()
    if("call" in b):
        c=input("TO WHOM TO YOU NEED TO CALL MENTION : ").split(" ")
        if(c[1] in g):
            print(f"CALLING  {c[1]} IS PROGRESSING.......")
    elif("open" in b):
            c=input("WHAT APP DO YOU NEED TO  OPEN : ")
            print(f"YOUR {c} APP IS OPENINING.......")
    elif("search" in b):
            c=input("WHAT DO YOU NEED TO BE SEARCHED : ")
            print(f"YOUR {c} DATA IS PROGRESSING .......")
    elif("increase sound" in b):
            print("YOUR SOUND IS INCREASE TO THE MAX .")
    elif("decrease sound" in b):
            print("YOUR SOUND IS DECREASE TO THE LOW .")
    else:
        print("CAN'T UNDERSTAND WHAT YOUR ARE SAYING .")
    
