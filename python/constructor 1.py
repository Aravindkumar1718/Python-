class Tel:

    def __init__ (this,model, year, sp,camera=1,storage="2GB"):
        this.camera = camera
        this.year = year
        this.speaker = sp 
        print('Tel constuctor called...')

    def makeCall(this, number):
        if (number.isnumeric()):
            print (f'calling {number}...')
        elif(persn.lower()in this.contact):
            print(f'calling {number}...')

        else:
            print('Invalid number')
        

    def addContact(this,user):
        this.contact.append(user.lower())

bs = Tel ('A24',2023,1)

print(bs.model)

bs.makeCall("java")

print('\n')
