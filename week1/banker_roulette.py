"""
# banker roulette
import random
names = input("Give me all the names, seperated by a comma.")
nam = names.split(",")

num = len(nam)  

choice = random.randint(0, num - 1)
print(f"Person paying is {choice}")

ch = random.choice(nam)
print(ch)
"""

# reviewing basics at the start of another year 2026
import random 
na = input(" Input all the names separating using a comma.")
n = len(na)

no = len(na)

choose = random.randint(0, no -1)
print(f"{choose}, is paying this time.")

choice = random.choice("choose")
print(choice)