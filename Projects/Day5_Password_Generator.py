#🚨Password Generator Project
import random

letters = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
  'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))
easy_passwd = ""
#Eazy Level - Order not randomised:
for char in range(1, n_letters + 1):
    easy_passwd += random.choice(letters)
for char in range(1, n_symbols + 1):
    easy_passwd += random.choice(symbols)
for char in range(1, n_numbers + 1):
    easy_passwd += random.choice(numbers)
print("Eazy password:", easy_passwd)
#Hard Level - Order of characters randomised:
hard_passwd = ""
passwd_list = []
for char in range(1, n_letters + 1):
  passwd_list.append(random.choice(letters))
for char in range(1, n_symbols + 1):
  passwd_list.append(random.choice(symbols))
for char in range(1, n_numbers + 1):
  passwd_list.append(random.choice(numbers))
print(passwd_list)
random.shuffle(passwd_list)
print(passwd_list)
for new in passwd_list:
  hard_passwd += new
print("Hard password:", hard_passwd)