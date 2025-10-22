# Class 12: Python Dictionaries Practice

# Creating a dictionary
student = {
    "name": "Rafi",
    "age": 15,
    "class": "Seven",
    "marks": {"math": 85, "english": 90, "science": 80}
}

print("=== Student Information ===")
print("Name:", student["name"])
print("Age:", student["age"])
print("Class:", student["class"])
print("Marks:", student["marks"])

# Accessing individual marks
print("\nMath Marks:", student["marks"]["math"])

# Adding a new key-value pair
student["grade"] = "A"
print("\nAfter adding grade:", student)

# Updating existing value
student["age"] = 16
print("\nAfter updating age:", student)

# Deleting a key
del student["class"]
print("\nAfter deleting class key:", student)

# Looping through keys and values
print("\n=== All Details ===")
for key, value in student.items():
    print(f"{key} → {value}")

# Checking if a key exists
if "marks" in student:
    print("\n'Marks' key exists in dictionary!")

# Get method with default value
city = student.get("city", "Not Provided")
print("\nCity:", city)
