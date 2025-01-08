# banker roulette
import random
names = input("Give me all the names, seperated by a comma.")
nam = names.split(",")

num = len(nam)  

choice = random.randint(0, num - 1)
print(f"Person paying is {choice}")

ch = random.choice(nam)
print(ch)

