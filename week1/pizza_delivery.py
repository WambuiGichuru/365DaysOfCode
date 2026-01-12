"""
#pizza delivery
print("Welcone to Pizza Deli!")
p = input("What size of pizza do you want? S, M or L?")
pep = input("Do you want pepperoni? Y or N")
che = input("Do you want cheese? Y or N")
bill = 0
if p == "S":
    bill += 15
    print("Small pizzas are: $15")
elif p == "M":
    bill += 20
    print("Medium pizzas are: $20")
else:
    bill += 25
    print("Large pizzas are: $25")

if pep == "Y":
    if p == "S":
        bill +=2
    else:
        bill +=3

if che == "Y":
    bill +=1
print(f"Final bill: ${bill}")
"""

# trying this again jameniiii, na vile nimechoka. pizza delivery code
print('Welcome to Pizza Palace! How can I help you?')
p = input("What pizza size do you want? S, M or L")
pep = input("Do you want pepperoni with that? Y or N")
che = input("How about some cheese on it? Y or N")

# bill counter
bill = 0

if p == "S":
    bill +=15
    print("Small pizzas are: $15")
elif p == "M":
    bill +=20
    print("Medium pizzas are: $20")
else:
    bill +=25
    print("Large ones are: $25")

#extras counter
if pep == "Y":
    if p == "S":
        bill +=2
    else:
        bill +=3


#cheese 
if che == "Y":
    bill +=1

print(f'Final bill is ${bill}')
