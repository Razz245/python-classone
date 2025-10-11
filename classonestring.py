# Strings
print("Hello from classone!")
print('Hello World')
print("""This string runs multiple lines""") #Triple Quote for multriline strings
print("This is a "+" string") #We can concatenate strings with +
print('\n') #New line
print('Test that new line out')

#sindle Quote
text1 = 'Hello'
print(text1)

#Double Quote
text2 = "Hello"
print(text2)
#Triple Quote
# ৩. Triple quote (একাধিক লাইন লেখার জন্য)
text3 = '''This is
a multi-line
string.'''
print(text3)

#String slicing
word = "Python"
print(word[0]) #First character
print(word[1]) #Second character
print(word[2]) #Third character
print(word[3]) #Fourth character
print(word[4]) #Fifth character
print(word[5]) #Sixth character
print(word[-1]) #Last character
print(word[-2]) #Second last character
print(word[-3]) #Third last character

#ImportentString Methods
txt = " Hello, World! "
print(word.upper()) #Convert to uppercase
print(word.lower()) #Convert to lowercase
print(word.capitalize()) #Capitalize first letter
print(txt.strip()) #Remove whitespace from start and end
print(txt.replace("H", "J")) #Replace H with J
print(txt.split(",")) #Split string into list at comma
print(len(word)) #Length of string
print(word[0:3]) #Substring from index 0 to 2
print(word[2:]) #Substring from index 2 to end
print(word[:4]) #Substring from start to index 3
print(word[1:5]) #Substring from index 1 to 

#String Concatenation
first = "Hello"
second = "World"
result = first + " " + second
print(result) #Output: Hello World

#Part TWO
name= ('Rashin Rabindra')
age= 22
print('My name is', name, 'and I am', age, 'years old.')#Using commas
print('My name is ' + name + ' and I am ' + str(age) + ' years old.')#Using +

txt = "Python Programming"
print("Length of the string:", len(txt)) #Length of string

quote = "learning python is fun"
print(quote.capitalize()) #Capitalize first letter
print(quote.title()) #Capitalize first letter of each word
print(quote.count("n")) #Count occurrences of 'n'
print(quote.find("python")) #Find position of 'python'
print(quote.replace("fun", "awesome")) #Replace 'fun' with 'awesome'
print(quote.split()) #Split string into list of words
print(quote.startswith("learning")) #Check if string starts with 'learning'
print(quote.endswith("fun")) #Check if string ends with 'fun'
print(quote.lower()) #Convert to lowercase
print(quote.upper()) #Convert to uppercase
print(quote.strip()) #Remove whitespace from start and end
print(quote.isalpha()) #Check if all characters are alphabetic
print(quote.isdigit()) #Check if all characters are digits
print(quote.isalnum()) #Check if all characters are alphanumeric
print(quote.index("python")) #Find index of 'python'
print(quote.rfind("n")) #Find last occurrence of 'n'
print(quote.center(50)) #Center string in a field of width 50
print(quote.ljust(50)) #Left justify string in a field of width 50
print(quote.rjust(50)) #Right justify string in a field of width 50
print(quote.zfill(50)) #Pad string with zeros to width 50

print(quote.isalpha()) # False, কারণ স্পেস আছে (alphabet নয়)
print("Python".isalpha()) # True
print("123".isdigit()) # True
print("Python3".isalnum()) # True

#Cute Output Format
print("\n--- String Slicing ---")
word = "Python"
print(word[0])
print(word[-1])

print("\n--- String Methods ---")
txt = " Hello, World! "
print(txt.strip())
print(txt.upper())

