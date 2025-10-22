# classnineprojectacalculator_advanced.py

print("=== Advanced Calculator ===")
while True:
    first = input("Enter first number (or 'exit' to quit): ")
    if first.lower() == 'exit':
        print("Calculator exited.")
        break
    second = input("Enter second number (or 'exit' to quit): ")
    if second.lower() == 'exit':
        print("Calculator exited.")
        break
    operator = input("Enter operator (+, -, *, /): ")
    if operator.lower() == 'exit':
        print("Calculator exited.")
        break

    try:
        num1 = float(first)
        num2 = float(second)
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero!")
                continue
            result = num1 / num2
        else:
            print("Invalid operator!")
            continue
        print(f"Result: {result}")
    except ValueError:
        print("Invalid number input! Please enter numeric values.")
