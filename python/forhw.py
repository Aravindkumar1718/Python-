#PATTERN-1

n = int(input("Enter the number of rows:"))   
for i in range(0, n):       
        for j in range(0, i + 1):             
            print("* ", end="")         
        print() 


#PATTERN-2


n = int(input("Enter the number of rows:"))   
for i in range(1, n+1):       
        for j in range(1, i + 1):             
            print(j, end=" ")         
        print() 



#PATTERN-3
        
n = int(input("Enter the number of rows:"))  
for i in range(1, 5):  
    for j in range(1, i + 1):   
        a = chr(n)  
        print(a, end=' ')  
        n += 1  
    print()  


#PATTERN-4

print("\n")
print (2+2+1+2) 
for i in range (n) :
    l = len(str(i))
print(f"{'0'*(2-1)}{i}")


#PATTERN -5

n = int(input("Enter the number of rows:"))   
for i in range(n):       
        for j in range(1, i + 1):
            print(j, end=" ")  
        print() 
