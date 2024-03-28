def create_user_list():

    userDataStr=open('f2.txt','r').read()
    allUser=userDataStr.split('\n')
    userObj=[]
    for user in allUser:
        user_list=user.split()
        print("Name : ",user_list[0])
        print("age  :",user_list[1])
        print("Email:",user_list[2])
        print("-"*50)
        
            

                
create_user_list()
