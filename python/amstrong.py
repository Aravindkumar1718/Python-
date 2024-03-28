a=int(input("Enter a number in three digit only: "))
b=a//100
print(b)
c=a%100
print(c)
d=c//10
print(d)
e=c%10
print(e)
num=(b**3)+(d**3)+(e**3)
if num==a:
    print(f"{a} is an Armstrong number")
else:
    print(f"{a} is not an Armstrong number")
