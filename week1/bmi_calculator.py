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
        