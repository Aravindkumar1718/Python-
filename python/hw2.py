n = "hi!have?are#you@"
result =chr(45)
print(result)
allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
for char in n:
    if char in allowed_chars:
        result += char
print(result)  

a = "hi! have? are# you@".split()
for i in a:
  print(type(a))
