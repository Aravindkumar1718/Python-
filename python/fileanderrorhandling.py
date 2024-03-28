yearStr= input ("Enter your Birth Year :")

try:
    
    year = int (yearStr)

    if (year > 100):

    raise Exception ("Your age is too high and it is not possible for in here who are living in the world")
    print (2023-year)
    



except Exception as err: print("your not eligible :: ",err)
