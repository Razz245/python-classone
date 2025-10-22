#Python Loops Practice Plan (Basic → Advanced)
#Class Eight: Loops
#Basic For Loop
# This class demonstrates the use of loops in Python.
for i in range(5):
    print("Iteration:", i + 1)
    print("This line always executes.\n")
    print("\n")
#While Loop
    i = 1
    while i <= 5:
        print("Iteration:", i)
        i += 1
    #Nested Loops
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"i: {i}, j: {j}")

# Advanced Looping Techniques
for num in range(1, 5):
    print(i)
else:
    print("Loop completed.")

#Loops over data structures
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#Comprehension Loops (Advanced)
squares = [x**2 for x in range(1, 6)]
print(squares)

#Practice Parts Two: Loop Challenges
# Python Loops: Basic → Advanced Practice

print("=== 1. Basic For Loop ===")
for i in range(5):
    print("Number:", i)

print("\n=== 2. While Loop ===")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

print("\n=== 3. Nested Loop ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()

print("\n=== 4. Loop Control Statements (break, continue, pass) ===")
for i in range(1, 10):
    if i == 3:
        continue
    if i == 8:
        break
    print(i)
else:
    print("Loop ended normally")

print("\n=== 5. Loop with else ===")
for i in range(3):
    print("Iteration:", i)
else:
    print("Loop completed successfully!")

print("\n=== 6. Loop over Data Structures ===")
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print("Fruit:", fruit)

info = {"name": "Razz", "language": "Python", "version": 3.12}
for key, value in info.items():
    print(f"{key}: {value}")

print("\n=== 7. List Comprehension ===")
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print("Squares:", squares)

evens = [n for n in range(1, 20) if n % 2 == 0]
print("Even Numbers:", evens)

print("\n=== 8. Bonus: Pattern Printing ===")
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
