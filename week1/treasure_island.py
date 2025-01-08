# treasure island
print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")

turn = input("Do you want to go left or right? left or right?")

t = turn.lower()

if t == "left":
    act = input("Do you want to swim or wait for a boat? swim or wait?")
    a = act.lower()
    if a == "swim":
        door = input("Which door do you wish to open? red, yellow or blue?")
        d = door.lower()
        if d == "red":
            print("Too hot to handle! Walked into a room of fire.")
            print("Game over! Better Luck next time")
        elif d == "blue":
            print("Bad luck! Walked off a ledge.")
            print("Game over! Better luck next time")
        else:
            print("You found the treasure!")
            print("Congratulations! You win")
    else:
        print("Oops! Irresistable, you became crocodile dinner.")
        print("Game over! Better luck next time.")
else:
    print("Oh no!You fell into a hole!")
    print("Game over! Better luck next time")
