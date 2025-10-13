def function_name():
    print("This is a function from classfivefunction.py")

function_name()#Srting: name, full_name, city

#Function call
def say_hello():
    print("Hello Python!")

say_hello()   # এখানে ফাংশন কল করা হয়েছে

#Function with parameters (argument)
def greet(name):
    print("Hello,", name)

greet("Rashin")
greet("Eli")
greet("Razz")
greet("Alice")

#Return Function
def add(a, b):
    return a + b

result = add(5, 7)
print("Result:", result)
print("Result:", add(10, 15))
print("Result:", add(-3, 3))
print("Result:", add(2.5, 4.5))
print("Result:", add("Hello, ", "World!"))  # String concatenation

#Other examples of functions
def square(num):
    return num * num

def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Square of 4 =", square(4))
print("10 is", even_or_odd(10))
print("7 is", even_or_odd(7))
print("Square of 5.5 =", square(5.5))
print("Square of -3 =", square(-3))
print("Square of 0 =", square(0))
print("Square of 100 =", square(100))


#Function Practice
def my_name(Razz):
    print("My name is", Razz)
my_name("Razz")

#Function with Parameter (Addition)
def add_numbers(a, b):
    print("Sum:", a + b)
    
add_numbers(10, 20)

# Function with Logic (Even or Odd)
def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")
check_even_odd(15)
check_even_odd(8)

#Function with Loop (Sum of list)
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("Sum of list:", sum_of_list([1, 2, 3, 4, 5]))


#Function with Condition and Return (Largest number finder)
def largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print("Largest number is:", largest_number(10, 20, 15))
print("Largest number is:", largest_number(-5, -10, -3))
print("Largest number is:", largest_number(7, 7, 7))
print("Largest number is:", largest_number(0, 0, -1))
print("Largest number is:", largest_number(100, 50, 75))
print("Largest number is:", largest_number(1.5, 2.5, 2.0))
print("Largest number is:", largest_number(-1, 0, 1))
print("Largest number is:", largest_number(3, 3, 2))
print("Largest number is:", largest_number(5, 10, 10))
print("Largest number is:", largest_number(0, -1, -2))