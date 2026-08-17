weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters (e.g., 1.70): "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

# شروط تصنيف الوزن
if bmi < 18.5:
    print("Status: Underweight (نحافة)")
elif bmi >=18.5 and bmi < 25:
    print("Status: Normal weight (وزن مثالي)")
elif bmi >= 25 and bmi < 30:
    print("Status: Overweight (وزن زائد)")
else:
    print("Status: Obesity (سمنة)")