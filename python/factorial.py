
n=int(input("Enter the value of n="))
n3=1
if(n<0):
    print("It is negative number can not be used for factorial.")
elif(n==0):
    print("The factorial of 0 is 1.")
else:
    for i in range(1,n+1):
        
        n3=i*n3
print(n3)
print("\n")
    
