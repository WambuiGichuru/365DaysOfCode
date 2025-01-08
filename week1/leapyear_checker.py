print("Welcome to a leap year checker")
year = int(input("What year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's a leap year")
        else:
            print("Not a leap year")
    else:
        print("It is a leap year")
else:
    print(" Sorry, not a leap year.")
    