#String Revised
# Demonstrating various string methods in Python
#String Operations Recap
text = "Python Programming"
print(len(text))            # Length of string
print(text.upper())         # All uppercase
print(text.lower())         # All lowercase
print(text.title())         # Each word title case
print(text.replace("Python", "Java"))  # Replace
print(text.find("Pro"))     # Finds index

#String Slicing
s = "Hello World"
print(s[0:5])   # Hello
print(s[6:])    # World
print(s[-5:])   # World
print(s[::-1])  # Reverse string

#Looping Through Strings
for char in s:
    print(char)
    
#String Concatenation & Repetition
a = "Data"
b = "Science"
print(a + " " + b)  # Concatenation
print(a * 3)        # Repetition

#Checking Substrings
name = "Artificial Intelligence"
print("Intel" in name)      # True
print("intel" not in name)  # True (case-sensitive)

#Useful String Methods
text = "  machine learning  "
print(text.strip())
print(text.split())
print("-".join(["AI", "ML", "DL"]))
print(text.startswith("  ma"))  # True
print(text.endswith("ning  "))   # True
print(text.count("a"))          # Count occurrences
print(text.isalpha())        # False (contains spaces)
print(text.isdigit())        # False
print(text.isalnum())       # False (contains spaces)
print(text.capitalize())  # Capitalize first letter
print(text.center(30, '*'))  # Centered with padding
print(text.zfill(30))      # Zero fill

#String Immutability Example
name = "Python"
# name[0] = "J"  # ❌ Error: strings are immutable
name = "J" + name[1:]  # ✅ Correct way
print(name)


#Mini Project: Palindrome Checker
word = input("Enter a word: ").lower()
if word == word[::-1]:
    print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")


print("\n=== End of String Practice ===")
print()