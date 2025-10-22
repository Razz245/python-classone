#Class Seven: Conditional Statements
# This class demonstrates the use of conditional statements in Python.
# It covers if, elif, and else statements with examples.
# Conditional Statements Practice

# Part 1: Simple if statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
print("This line always executes.\n")

# Part 2: if-else statement
marks = int(input("Enter your marks: "))
if marks >= 50:
    print("You passed the exam.")
else:
    print("You failed the exam.")
print("\n")

# Part 3: if-elif-else ladder
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
print("\n")

# Part 4: Nested if
x = int(input("Enter X value: "))
y = int(input("Enter Y value: "))
if x > 0:
    if y > 0:
        print("Both X and Y are positive.")
    else:
        print("X is positive but Y is not positive.")
else:
    print("X is not positive.")
print("\n")

# Part 5: Practice Challenge
temperature = int(input("Enter temperature in Celsius: "))
if temperature > 35:
    print("It's a hot day.")
elif temperature >= 25:
    print("It's a warm day.")
elif temperature >= 15:
    print("It's a cool day.")
else:
    print("It's a cold day.")
print("\n")

# End of Class Seven


#Conditinal Statements Practice

def drink(money):
    if money >= 50:
        return "You can buy a drink."
    else:
        return ("You cannot buy a drink.")
print(drink(60))
print(drink(30))

def alcohol(age, money):
    if(age >= 18) and (money >= 50):
        return "You can buy alcohol."
    elif(age >= 18) and (money < 50):
        return "Come back with more money."
    elif(age < 18) and (money >= 50):
        return "You are underage."
    else:
        return "You are underage and have no money."
print(alcohol(20, 60))
print(alcohol(20, 30))
print(alcohol(16, 60))
print(alcohol(16, 30))

print("Class Seven: Conditional Statements Practice")
print("---")

# Part 1: Age check
age = int(input("Enter your age: "))
if age >= 18:
    print("✅ You are eligible to vote.")
else:
    print("❌ You are not eligible to vote.")

print("---")

# Part 2: Exam marks
marks = int(input("Enter your exam marks (0-100): "))
if marks >= 50:
    print("✅ You passed the exam.")
else:
    print("❌ You failed the exam.")

print("---")

# Part 3: Number sign check
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

print("---")

# Part 4: Nested if example
x = int(input("Enter X value: "))
y = int(input("Enter Y value: "))
if x > 0:
    if y > 0:
        print("Both X and Y are positive.")
    else:
        print("X is positive but Y is not positive.")
else:
    print("X is not positive.")

print("---")

# Part 5: Temperature check
temperature = int(input("Enter temperature (Celsius): "))
if temperature > 35:
    print("🔥 It's a hot day.")
elif temperature >= 25:
    print("🌞 It's a warm day.")
elif temperature >= 15:
    print("🌤️ It's a cool day.")
else:
    print("❄️ It's a cold day.")
print("--- End of Practice ---")