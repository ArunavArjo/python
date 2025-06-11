height = float(input("Enter your height in meters:"))
weight = float(input("Enter your weight in kilograms:"))

BMI = weight/(height**2)
print(f"Your BMI is{BMI:.2f}")

if BMI < 18.5:
    print("You are underweight")
elif BMI < 25:
    print("You are normal weight")
elif BMI < 30:
    print("You are overweight")
elif BMI < 35:
    print("You are severly overweight")
elif BMI < 40:
    print("You are obese")
else:
    print("You are extremly obese")