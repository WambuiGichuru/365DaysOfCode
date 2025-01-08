#love calculator
print("Welcome to the love calculator")
m = input("What is your name?")
n = input("What is their name?")
names = m + n
names_lower = names.lower()

t = names_lower.count("t")
r = names_lower.count("r")
u = names_lower.count("u")
e = names_lower.count("e")

first = t + r + u + e

l = names_lower.count("l")
o = names_lower.count("o")
v = names_lower.count("v")
e = names_lower.count("e")

second = l + o + v + e

score = str(first)+str(second)

if score < "10" or score > "90":
    print(f"Your score is {score}%, you go together like coke and mentos.")
elif score > "40" or score < "50":
    print(f"Your score is {score}%, you are alright together.")
else:
    print(f"Your score is {score}")
    