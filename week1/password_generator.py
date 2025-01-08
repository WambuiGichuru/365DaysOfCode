# password generator
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
        'n','o','p','q','r','s','t','u','v','w','x','y','z'
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','+','(',')']

print("Welcome to the PyPassword Generator")
l = int(input("How many letters would you like in your password? "))
s = int(input(f"How many symbols would you like? "))
n = int(input(f"How many numbers would you like? "))

password = ''

for p in range(1, l+ 1):
    password += random.choice(letters)

for p in range(1, s +1):
    password += random.choice(symbols)

for p in range(1, n +1):
    password += random.choice(numbers)
print(password)
