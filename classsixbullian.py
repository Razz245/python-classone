# Boolean expression — এমন একটি expression যার ফলাফল হয় True বা False

# Part 1: Boolean examples
print(5 > 3)     # True
print(10 == 5)   # False
print(7 != 2)    # True

# Relational Operators (তুলনা করার অপারেটর)
# ==, !=, >, <, >=, <=

# Practice
a = 10
b = 20

print(a < b)               # True
print(a == 10)             # True
print(a != b)              # True
print(a > 5 and b > 15)    # True
print(a < 5 or b < 15)     # False
print(not(a > b))          # False

# Part 2: True or False — Predict the output
print(5 > 3)       # True
print(7 == 8)      # False
print(10 != 10)    # False
print(15 >= 10)    # True
print(20 < 5)      # False
print(12 <= 12)    # True
print(4 + 3 == 7)  # True
print(8 - 2 > 10)  # False

# Part 3: Logical Operators (and, or, not)
a = 5
b = 10

print(a < 10 and b > 5)    # True
print(a == 5 or b == 5)    # True
print(a > 10 and b < 20)   # False
print(not(a == 5))          # False
print(a != b or b == 10)    # True
print((5 > 3) and (10 < 15)) # True

# Part 4: Fill in the blanks (Predict the output)
print(8 > 3)          # True
print(4 == 4)         # True
print(4 != 5)         # True
print(5 < 2)          # False
print(5 >= 5)         # True
print(5 <= 3)         # False
print(10 > 5 and 2 < 3)      # True
print(15 == 15 or 10 < 5)    # True
print(20 != 20 and 5 > 1)    # False
print(23 < 30 or 40 == 50)   # True
print(50 > 60)                # False
print(70 <= 70)               # True

# Part 5: Small Challenge — Input + Boolean
time = int(input("Enter your Time: "))
can_meet = time >= 18
print("You can meet:", can_meet)

age = int(input("Enter your age: "))
can_vote = age >= 18
print("You can vote:", can_vote)
