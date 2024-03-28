b = ["-","-","-","-","-","-","-","-","-"]
def fun():
    if(b[0]=='X'and b[1]=='X' and b[2]=='X')or(b[3]=='X'and b[4]=='X' and b[5]=='X')or (b[6]=='X'and b[7]=='X' and b[8]=='X')or(b[0]=='X'and b[3]=='X' and b[6]=='X')or(b[1]=='X'and b[4]=='X' and b[7]=='X')or(b[2]=='X'and b[5]=='X' and b[8]=='X')or(b[0]=='X'and b[4]=='X' and b[8]=='X')or(b[1]=='X'and b[4]=='X' and b[7]=='X')or(b[2]=='X'and b[4]=='X' and b[6]=='X'):
        print("X is Winner")
        return True
    elif(b[0]=='O'and b[1]=='O' and b[2]=='O')or(b[3]=='O'and b[4]=='O' and b[5]=='O')or (b[6]=='O'and b[7]=='O' and b[8]=='O')or(b[0]=='O'and b[3]=='O' and b[6]=='O')or(b[1]=='O'and b[4]=='O' and b[7]=='O')or(b[2]=='O'and b[5]=='O' and b[8]=='O')or(b[0]=='O'and b[4]=='O' and b[8]=='O')or(b[1]=='O'and b[4]=='O' and b[7]=='O')or(b[2]=='O'and b[4]=='O' and b[6]=='O'):
        print("O is Winner")
        return True
    return False
    

def player(val):
    c=int(input("Enter the value of number="))
    if(val%2==0):
        b[c-1]="X"
    else:
        b[c-1]="O"

def board():
    for i in range(0,len(b)):
        print(b[i],end="  ")
        if((i+1)%3==0):
            print()
            print()
    
board()
count = 0
while("-" in b):
    gs=fun()
    if(gs):
        break
    player(count)
    board()
    count+=1
    count-=2





    
