"""
# BMI Calculator
print("Welcome to the BMI calculator")
height = float(input("Please enter your height in m: "))
weight = int(input("Please enter your weight in kg: "))

BMI = round((weight/height**2),1)

if BMI < 18.5:
    print(f"Your BMI is: {BMI} , You are underweight")
elif BMI < 25:
    print(f"Your BMI is: {BMI} , You are normal weight")
elif BMI < 30:
    print(f"Your BMI is: {BMI} , Your are overweight")
elif BMI < 35:
    print(f"Your BMI is: {BMI} , You are obese")
else:
    print(f"Your BMI is: {BMI} , Your are clinically obese")

"""
    
# recoding this a year later to review my basics and ensure they are stil intact
print('This is a BMI Calculator')
heig = float(input('Enter your height in metres:'))
weig = int(input('Enter weight in kgs: '))
B = round((weig/heig**2),1)

if B < 18.5:
    print(f"BMI is: {B}, you are underweight")
if B < 25:
    print(f"BMI is: {B}, you are normal weight")
if B < 30:
    print(f"BMI is: {B}, you are overweight")
if B < 35:
    print(f"BMI is: {B}, you are obese")
else:
    print(f"BMI is: {B}, you are clinically obese")
