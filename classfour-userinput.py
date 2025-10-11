#  User Input
#simple Input
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome!")
#input always takes input as string
#Type Conversion
age = int(input("Enter your age: ")) # Convert input to integer
print("You are " + str(age) + " years old.")

#Number Input
#Integer input
age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")

#Float input
height = float(input("Enter your height in meters: "))
print("You are " + str(height) + " meters tall.")

#Using Input in Calculations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum = num1 + num2
print("Sum =", sum)

#f-Strings (Recommended)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} years old.")
print(f"In 5 years, I will be {age + 5} years old.")
print(f"Next year, I will be {age + 1} years old.")
print(f"Double my age is {age * 2}.")
print(f"Half my age is {age / 2}.")
print(f"My age squared is {age ** 2}.")
print(f"My age plus 10 is {age + 10}.")
print(f"My age minus 5 is {age - 5}.")

