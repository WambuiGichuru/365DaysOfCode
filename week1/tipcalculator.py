# Tip Calculator
print("Tip Calculator")
b = int(input("What is the Bill Amount: $"))
p = int(input("How many people do you want it split by?"))
t = int(input("What is the tip amount you want to give? 10, 12 or 15?"))

tip = b * (t/100)
bill = round((b + tip)/p,2)

print(f"Bill is: ${bill} per person")