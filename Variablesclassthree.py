#Variables in Python
# A variable is a container for storing data values.Rules for defining variables:letters, numbers, and underscores. Cannot start with a number. Case-sensitive. No spaces or special characters.
#case-sensitive: name, Name and NAME are three different variables.
#Dont use Python keywords as variable names.
#Examples of valid variable names:
#Srting: name, full_name, city
#Single word: age, name, total
1.
# Strings
name = "Razz"
city = "Dhaka"
country = "Bangladesh"

# Integer
age = 22
year = 2025

# Float
height = 5.9
weight = 70.5

# Boolean
is_student = True
is_teacher = False

2. #Printing Variables

print(name) # Output: Razz
print(city) # Output: Dhaka
print(country) # Output: Bangladesh
print(age) # Output
print(year) # Output: 2025
print(height) # Output: 5.9
print(weight) # Output: 70.5
print(is_student) # Output: True
print(is_teacher) # Output: False
print("My name is", name, "and I live in", city + ",", country + ".") #Using commas
print("My weight is", weight, "kg.")
print("Am I a student?", is_student)
print("Am I a teacher?", is_teacher)

#Vables can be reassigned to different values and types:
name = "Rashin Rabindra"
x = 22
X = "Twenty Two"
print(name) # Output: Rashin Rabindra
print(x)    # Output: 22
print(X)    # Output: Twenty Two

#Basic Methods (Strings & Numbers)
text = "python programming"
print(text.upper())     # 'PYTHON PROGRAMMING'
print(text.lower())     # 'python programming'
print(text.title())     # 'Python Programming'
print(text.capitalize())# 'Python programming'
print(text.replace("python", "Python")) # Replace substring
print(len(text))        # Length of string
print(text.split())     # Split into list
print(text.startswith("py")) # True
print(text.endswith("ing"))  # True
print(text.find("gram"))     # 10
print(text.count("o"))       # 2
print(text.isalpha())        # False (space is not alphabetic)
print(text.isdigit())        # False
print(text.isalnum())        # False (space is not alphanumeric)
print(text.index("pro"))     # 7
print(text.rfind("m"))      # 12
print(text.center(30))      # Centered in a field of width 30
print(text.ljust(30))      # Left justified in a field of width 30
print(text.rjust(30))      # Right justified in a field of width 30
print(text.zfill(30))      # Padded with zeros to width 30
print(text.strip())      # Remove leading/trailing whitespace
print(text.isalpha()) # False, because of space

# Number Methods & Arithmetic Operations

x = -50

print(abs(x))               # Absolute value → 50
print(round(3.14159, 2))    # Round to 2 decimal → 3.14
print(pow(2, 3))            # 2^3 → 8
print(max(10, 20, 30))      # Maximum → 30
print(min(10, 20, 30))      # Minimum → 10
print(sum([10, 20, 30]))    # Sum of list → 60
print(int(50.99))           # Convert to integer → 50
print(float(50))            # Convert to float → 50.0
print(complex(2, 3))        # Complex number → (2+3j)
print(divmod(50, 30))       # Quotient & remainder → (1, 20)

# Mathematical Operations
print(x % 7)                # Remainder of division → 1
print(x // 7)               # Quotient of division → -8
print(x ** (1/2))           # Square root using exponentiation → complex
print((x * 30) ** 0.5)      # Square root of product → complex
print((x + 30) / 2)         # Average of two numbers → -10.0
print((x + (30 * 2) - (10 / 2)))  # Combined → -10.0
print((x * (30 + 20) / 10))       # Combined with parentheses → -250.0
print((x + 30 * (2 - 1)))         # Combined with subtraction → -20
print(((x + 30) * (2 + 3)))       # Combined with addition → -100
print((x + 30) * 2)               # Using parentheses → -40

# Extra Examples
print(50 + 30 * (2 - 1))          # Combined with subtraction → 80
print((50 + 30) * (2 + 3))        # Combined with addition → 400
print((50 + 30) * 2)              # Using parentheses → 160

# Type Conversion Examples

a = 10       # int
b = 5.5      # float

print(int(b))        # 5
print(float(a))      # 10.0
print(str(a))        # '10'
print(str(b))        # '5.5'

print(int("20"))     # 20
print(float("20.5")) # 20.5
print(str(100))      # '100'
print(str(99.99))    # '99.99'
print(int(99.99))    # 99

# Error examples (commented out to avoid runtime errors)
# print(float("abc")) # ValueError: cannot convert 'abc' to float
# print(int("abc"))   # ValueError: cannot convert 'abc' to int

print(str(True))     # 'True'
print(int(False))    # 0
print(float(True))   # 1.0
print(str(None))     # 'None'

# Error examples with None
# print(int(None))    # TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
# print(float(None))  # TypeError: float() argument must be a string or a number, not 'NoneType'

print(str([1, 2, 3])) # '[1, 2, 3]'

# Error example with list
# print(int([1, 2, 3])) # TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
