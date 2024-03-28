####  BIKE #####
print("\t\t\t BIKE\n\n")
class BIKE:
    def __init__(self, name):
        self.name = name
    def say(self):
        print('My bike company name is', self.name)
    def model(self,names):
        print('My bike model is', names)

b = BIKE('Royal Enfield')
b.say()
b.model('Classic_350')
print()
print()
print("~"*50)
##### MOBILE #####
print("\t\t\t MOBILE\n\n")
class MOBILE:
    def __init__(self, name):
        self.name = name
        print("My Mobile Company name is ",self.name)
    def processor(self,pro):
        print('My MOBILE processor is', pro)
    def model(self,names):
        print('My MOBILE model is', names)

b = MOBILE('APPLE')
b.processor('Bionic')
b.model('14 Pro Max')
print()
print()
print("~"*50)


######   GUN  ###### 
print("\t\t\t GUN\n\n")

class GUN:
    def __init__(self, name):
        self.name = name
        print("My GUN name in KGF is",self.name)
    def type(self,pro):
        print('My GUN type is', pro)
    def model(self,names):
        print('My GUN model is', names)

b=GUN('Kalashnikov')
b.type('RIFLE')
b.model('AK47')
print()
print()
print("~"*50)

###### TV #######
print("\t\t\t TV\n\n")


class TV:
    def __init__(self, name):
        self.name = name
        print("My TV name is ",self.name)
    def type(self,pro):
        print('My TV type is', pro)
    def size(self,size):
        print(f'My TV size is {size} inches')

b=TV('REDMI')
b.type('ANROID TV OR SMART TV')
b.size('55')

print()
print()
print("~"*50)



