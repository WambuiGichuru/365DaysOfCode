import random
choi = ('rock', 'paper','scissors')
comp = random.choice(choi)
choices = ('r','p','s')
# display question


while True:
    user = input("What do you pick? r/p/s : ").lower()
    if user not in choices:
        print("Invalid choice!")

    #compare against the computers play
    if comp == "rock" and "r":
        print(f"Computer chose {comp}\n You chose {user}\n It's a tie!")
    elif comp == "rock" and user == "p":
        print(f"Computer chose {comp}\n You chose {user}\n You win!")
    elif comp == "rock" and user == "s":
        print(f"Computer chose {comp}\n You chose {user}\n You lose!")
    elif comp == "paper" and user == "r":
        print(f"Computer chose {comp}\n You chose {user}\n You lose!")
    elif comp == "paper" and user == "p":
        print(f"Computer chose {comp}\n You chose {user}\n It's a tie")
    elif comp == "paper" and user == "s":
        print(f"Computer chose {comp}\n You chose {user}\n You win")
    elif comp == "scissors" and user == "r":
        print(f"Computer chose {comp}\n You chose {user}\n You win!")
    elif comp == "scissors" and user == "p":
        print(f"Computer chose {comp}\n You chose {user}\n You lose")
    elif comp == "scissors" and user == "s":
        print(f"Computer chose {comp}\n You chose {user}\n It's a tie")

    cont = input('Continue? y/n :').lower()
    if cont == 'n':
        break
