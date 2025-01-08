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
