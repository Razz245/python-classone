# === Class 11: Tuples in Python ===

# A tuple is like a list but immutable (cannot be changed after creation)
print("=== Tuple Basics ===")
my_tuple = (10, 20, 30, 40, 50)
print("Tuple:", my_tuple)
print("Type:", type(my_tuple))
print("Length:", len(my_tuple))

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Loop through tuple
print("\n=== Loop through tuple ===")
for num in my_tuple:
    print(num)

# Tuple slicing
print("\n=== Tuple slicing ===")
print("my_tuple[1:4]:", my_tuple[1:4])

# Tuple unpacking
print("\n=== Tuple unpacking ===")
a, b, c, d, e = my_tuple
print("a:", a, "b:", b, "c:", c, "d:", d, "e:", e)

# Nested tuples
print("\n=== Nested Tuples ===")
nested = (1, 2, (3, 4, 5))
print("Nested Tuple:", nested)
print("Access nested element:", nested[2][1])

# Tuple methods
print("\n=== Tuple Methods ===")
t = (10, 20, 20, 30, 20, 40)
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))

# Tuple immutability demonstration
print("\n=== Tuple Immutability ===")
try:
    my_tuple[0] = 99
except TypeError:
    print("❌ Cannot modify tuple elements — Tuples are immutable!")