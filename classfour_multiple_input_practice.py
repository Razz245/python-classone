# 🧮 Practice 1: BMI Calculator
print("\n=== 🏋️ BMI Calculator ===\n")

name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"\n{name}, your BMI is {bmi:.2f}.\n")

if bmi < 18.5:
    print("You are underweight.\n")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.\n")
elif 25 <= bmi < 29.9:
    print("You are overweight.\n")
else:
    print("You are obese.\n")


# 🧓 Practice 2: Simple Age Calculator
print("=== ⏳ Age Calculator ===\n")

current_year = int(input("Enter the current year: "))
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year

print(f"\nYou are {age} years old.\n")


# ➕ Practice 3: Calculate App
print("=== 🧠 Simple Calculator ===\n")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    print(f"\nThe sum is: {num1 + num2}\n")
elif operation == '-':
    print(f"\nThe difference is: {num1 - num2}\n")
elif operation == '*':
    print(f"\nThe product is: {num1 * num2}\n")
elif operation == '/':
    print(f"\nThe quotient is: {num1 / num2}\n")
else:
    print("\n❌ Invalid operation.\n")


# 🔢 Practice 4: Multiple Input in One Line
print("=== 📥 Multiple Input Example ===\n")

x, y, z = map(int, input("Enter three numbers separated by spaces: ").split())
print(f"\nYou entered:\n x = {x}\n y = {y}\n z = {z}\n")

#Challenge 1: Three Number Sum
x, y, z = map(int, input("Enter three numbers separated by spaces: ").split())
total = x + y + z
print(f"The sum of {x}, {y}, and {z} is {total}")

#hallenge 2: Average Finder
x, y, z = map(float, input("Enter three numbers separated by spaces: ").split())
avg = (x + y + z) / 3
print(f"The average of {x}, {y}, and {z} is {avg:.2f}")

#Challenge 3: Find Maximum & Minimum
x, y, z = map(int, input("Enter three numbers separated by spaces: ").split())
print(f"The maximum number is {max(x, y, z)}")
print(f"The minimum number is {min(x, y, z)}")

#Challenge 4: Reverse Order Print
x, y, z = map(int, input("Enter three numbers separated by spaces: ").split())
print(f"Reverse order: {z}, {y}, {x}")

#Challenge 5: Conditional Check
x, y, z = map(int, input("Enter three numbers separated by spaces: ").split())
count = sum(1 for n in [x, y, z] if n > 100)
print(f"There are {count} numbers greater than 100.")

