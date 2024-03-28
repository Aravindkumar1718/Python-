##user_list=[]
##num_users=3
##
##for i in range(num_users):
##    print(f"Enter details for User{i+1} :")
##    name = input("Name: ")
##    age = int(input("Age: "))
##    email = input("Email: ")
##for i in range(0,5):
##    i = {"name": name,"age": age,"email": email}
##    user_list.append(i)
##
##print(user_list)
##
##
##
##
##
##
##
users_list = []
user=5
for i in range(5):
    print(f"Enter details for User{i+1} :")
    name = input("Name: ")
    age = int(input("Age: "))
    email = input("Email: ")
    users_list.append(user)
##print("List of users:", users_list)
search = input("Enter the name to get the index: ")
if search in users_list:
    index= users_list.index(search)
##    print("Index of", search, "is:", index)
    print("User at the index:",users_list[index_to_get])
else:
    print("none")
