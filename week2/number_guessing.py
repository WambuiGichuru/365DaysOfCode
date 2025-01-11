#number guessing game
import random
#generate a random number between 0-100
num = random.randint(0,100)

while True:
    #handling an error in case of an invalid entry, eg letters
    try:
        #displaying question
        guess = int(input("Guess the number:"))
        # check the number if matches
        if guess > num:
            print("Too high! Guess again")
        elif guess < num:
            print("Too low! Guess again")
        elif guess == num:
            print("You got it!")
            break
    except ValueError:
        print("Please enter a valid number")
# continues till guess is correct