# fizzbuzz exercise
t = 0
for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
        