n=input("Enter your name:")
a=int(input("Enter your age:"))
g=input("Enter your gender:")
if g=="male" or g=="Male":
    if a>=18:
        print("MALE JOB")
    else:
        print("STUDENT JOB")
elif g=="female" or g=="Female":
    if a>=18:
        print("FEMALE JOB")
    else:
        print("STUDENT JOB")
