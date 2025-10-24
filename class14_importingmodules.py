# ==========================
# Class 14: Importing Modules in Python
# ==========================

# --- Math Module ---
import math
print("=== Math Module Examples ===")
print("Square root of 16:", math.sqrt(16))
print("Value of Pi:", math.pi)
print("Cosine of 0 degrees:", math.cos(math.radians(0)))
print("Factorial of 5:", math.factorial(5))
print("Power of 2^3:", math.pow(2, 3))

# More math functions
print(math.sqrt(25))       # Square root
print(math.pow(2, 5))      # 2^5
print(math.pi)             # π constant

# --- Importing specific functions ---
from math import sqrt, pow, pi
print("\n=== Importing Specific Functions ===")
print("Square root of 36:", sqrt(36))
print("3^4 =", pow(3, 4))
print("Pi constant:", pi)

print("\nHello, welcome to Class 14 on Importing Modules in Python!")
print("In this class, we will learn how to use modules to enhance our Python programs.")
print("Modules are pre-written code libraries that we can import and use in our own code.")

# --- Aliasing Modules ---
import math as m
print("\n=== Using Aliased Math Module ===")
print("Square root of 49:", m.sqrt(49))
print("Value of Pi:", m.pi)
print("Cosine of 60 degrees:", m.cos(m.radians(60)))
print("Factorial of 6:", m.factorial(6))
print("Power of 3^4:", m.pow(3, 4))
print(m.sqrt(81))       # Square root
print(m.pow(4, 2))      # 4^2
print(m.pi)             # π constant

print("Thank you for attending Class 14 on Importing Modules in Python!")

# --- Random Module ---
import random
print("\n=== Random Module Examples ===")
print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random float between 0 and 1:", random.random())
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))
print("Random sample of 3 elements from a list:", random.sample([1, 2, 3, 4, 5, 6], 3))

# shuffle() modifies the list in-place
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list:", my_list)

# --- Date & Time Module ---
import datetime
print("\n=== Date & Time Module Examples ===")
print("Current date and time:", datetime.datetime.now())
print("Current date:", datetime.date.today())
print("Current time:", datetime.datetime.now().time())
print("Formatted date:", datetime.datetime.now().strftime("%Y-%m-%d"))
# --- Making a Custom Module and Importing It ---
import class14_mymodulefile  # Custom module (create separately)

def main():
    return class14_mymodulefile.greet("Student")

def bye():
    return class14_mymodulefile.farewell("Student")

print("\n=== Custom Module Example ===")
print(main())
print(bye())
print("5 + 10 =", class14_mymodulefile.add(5, 10))

print("\nThank you for attending Class 14 on Importing Modules in Python!")
print("Goodbye!")

