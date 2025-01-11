# dice rolling game
import random
dice = (1,2,3,4,5,6)

while True:
    ques = str(input("Roll the dice? y/n"))
    q = ques.lower()

    if q == "y":
        er = random.choices(dice,k=2)
        print(er)
    elif q == "n":
        print("Okay, thanks for playing")
        break
    else:
        print("Invalid choice")

