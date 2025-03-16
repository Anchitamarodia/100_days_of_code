#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
finallist=[]
for i in range(0,nr_letters):
  randomletter=random.randint(0,len(letters)-1)
  letterlist=finallist.append(letters[randomletter])

for i in range(0,nr_symbols):
  randomsymbols=random.randint(0,len(symbols)-1)
  symbolslist=finallist.append(symbols[randomsymbols])

for i in range(0,nr_numbers):
  randomnumbers=random.randint(0,len(numbers)-1)
  numberslist=finallist.append(numbers[randomnumbers])


random.shuffle(finallist)
password=''
for i in finallist:
  password+=i

print(f"Your Generated Password is : {password}")


  

  






