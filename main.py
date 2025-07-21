# 🧮 BMI Calculator by Kavyashree Visaji

# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Output
print("\nEntered weight is:", weight, "kg")
print("Entered height is:", height, "m")
print("BODY MASS INDEX is:", round(bmi, 2))

# Classification
if bmi < 18.5:
    print("YOU ARE UNDERWEIGHT")
elif bmi < 25:
    print("YOU ARE NORMAL")
elif bmi < 30:
    print("YOU ARE OVERWEIGHT")
elif bmi < 35:
    print("YOU ARE OBESE (Class 1)")
elif bmi < 40:
    print("YOU ARE OBESE (Class 2)")
else:
    print("YOU ARE OBESE (Class 3)")
