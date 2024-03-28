print("\t\t\tA T M\n\n\n")
n=int(input("Enter the PIN number:")).isdigit()
print(n)
if n==1234:
      print("1.deposit\n2.withdraw\n3.balance ")
      a=(input("Enter the choices in  number:")).lower().isdigit()
      if a==1 or a=="deposit"or a=="one" :
          c=(input("Enter the  amount to be deposited:"))
          b=10000+c
          print("The total amount is:",b)
      elif a==2 or a=="withdraw" or a=="two" :
         w=int(input("Enter the amount to be withdraw:")).isdigit()
         if w<=5000 :
             t=5000-w
             print("The amount withdraw is:",w)
             print("The Balance amount is:",t)
         else:
             print("The amount is in insufficient amount in your account")
      elif a==3 or a=="balance" or a=="three":
          print("The Balance amount is 10000")
      else:
          print("Please enter the  correct choices from the top")
                   
else:
    print("The PIN in invalid")

               
         
      
