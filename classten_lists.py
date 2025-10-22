#Class Ten: Fata Structure Lists
fruits = ["apple", "banana", "cherry", "date"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]
print("Fruits List:", fruits)
print("Numbers List:", numbers)
print("Mixed List:", mixed)

#Indexing and Slicing
print("First fruit:", fruits[0])
print("Last number:", numbers[-1])
print("Sliced fruits (1 to 3):", fruits[1:3])
print("Every second number:", numbers[::2])
print("Reversed fruits:", fruits[::-1])
print()

#Changing List Elements
fruits[1] = "blueberry"
print("Updated Fruits List:", fruits)
fruits[2:4] = ["cantaloupe", "dragonfruit"]
print("Fruits List after slice update:", fruits)
fruits.append("elderberry")
print("Fruits List after append:", fruits)
fruits.insert(2, "fig")
print("Fruits List after insert:", fruits)
fruits.remove("apple")
print("Fruits List after remove:", fruits)

#Looping through Lists
for fruit in fruits:
    print("Fruit:", fruit)
print()

#Membership Testing
if "banana" in fruits:
    print("Banana is in the fruits list.")
    print()
else:
    print("Banana is not in the fruits list.")
    print()


#Sorting ও Reversing Lists
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

#Nested Lists
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[1][2])  # Output: 6
print(matrix)
print()

#List Comprehensions
squared_numbers = [x**2 for x in numbers]
print("Squared Numbers:", squared_numbers)

print("\n=== End of List Practice ===")