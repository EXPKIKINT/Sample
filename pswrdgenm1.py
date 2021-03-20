import random
def etc(upper,lower,num,symb,all):
    Uppercase_letters = "ABCDEFGHIGKLNMOPQRSTUVZYX"
    Lowercase_letters = Uppercase_letters.lower()
    Digits = "123456789"
    Symbols = "@#&-_+"
    upper,lower,num,symb = True,True,True,True
    all = ""

if etc(upper):
  etc += (all) 
  etc += (upper)
if erc(lower):
  etc+=(all) 
  etc+=(lower)
if etc(num):
  etc+=(all) 
  etc+=(num)
if etc(symb):
  etc+=(all) 
  etc+=(symb)

length = int(input ("Enter your length of the password :"))
amount = int(input("Enter your amount of the password :"))

for x in range(amount):
  password = "".join(random.sample(etc(all), length))
  print("\nRandom password is :\n %r\n" % (password))