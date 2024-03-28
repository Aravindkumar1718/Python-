class Mobile (Tel):

def _init_(this,m,mic, color, spk, camera) print('mobile constuctor called ")

super().___init_(m, mic, color, spk)

this.camera = camera

this.contact = []

def addContact (this, name): this.contact.append(name)

def makeCall (this, person): if (person.isnumeric()):

print (f" calling (person).. ") elif (person in this.contact):

print (f" calling (person}...")

else:

print('invalid contact')

:

mi = Mobile ("M4A", 1, "red", 2,2)

print (mi.contact)

mi.addContact ("python") mi.addContact ("java")

print (mi.contact)|

mi.makeCall("kdfdh")
