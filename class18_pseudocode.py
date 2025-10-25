#Pseudocode for a class that represents a simple bank account
# Define class BankAccount
# Class BankAccount:
#     # Define constructor with parameters: account_holder_name, initial_balance
#     Function __init__(self, account_holder_name, initial_balance):
#         # Set instance variable account_holder_name to parameter account_holder_name
#         self.account_holder_name = account_holder_name


# Practice 1: Simple Calculator with Error Handling

def get_number(prompt):
    """Get a valid number from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number!")

def get_operator():
    """Get a valid operator from user"""
    valid_operators = ['+', '-', '*', '/']
    while True:
        operator = input("Enter operator (+, -, *, /): ")
        if operator in valid_operators:
            return operator
        print("Error: Please enter a valid operator!")

# Main program
print("=== Simple Calculator ===")
num1 = get_number("Enter first number: ")
operator = get_operator()
num2 = get_number("Enter second number: ")

# Perform calculation
result = None
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero!")

# Display result
if result is not None:
    print(f"Result: {num1} {operator} {num2} = {result}")
    
#Practice 2: Student Grade System

def calculate_grade(score):
    """Calculate grade based on score"""
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def get_valid_score():
    """Get a valid score between 0-100"""
    while True:
        try:
            score = float(input("Enter student score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Error: Score must be between 0 and 100!")
        except ValueError:
            print("Error: Please enter a valid number!")

# Main program
print("=== Student Grade Calculator ===")
student_name = input("Enter student name: ")
score = get_valid_score()

grade = calculate_grade(score)
print(f"Student: {student_name}")
print(f"Score: {score}")
print(f"Grade: {grade}")

# Additional feedback
if grade == "F":
    print("Status: Failed - Needs improvement")
else:
    print("Status: Passed - Good job!")
    
# Practice 3: Bank Account System

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return True
        return False
    
    def display_balance(self):
        """Display current balance"""
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")
    
    def display_transactions(self):
        """Display transaction history"""
        print(f"\nTransaction History for {self.account_holder}:")
        for transaction in self.transaction_history:
            print(f" - {transaction}")

# Main program
def main():
    print("=== Simple Bank System ===")
    
    # Create account
    name = input("Enter account holder name: ")
    initial_deposit = float(input("Enter initial deposit: $"))
    account = BankAccount(name, initial_deposit)
    
    while True:
        print("\n=== Bank Menu ===")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            amount = float(input("Enter deposit amount: $"))
            if account.deposit(amount):
                print("Deposit successful!")
            else:
                print("Invalid deposit amount!")
                
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: $"))
            if account.withdraw(amount):
                print("Withdrawal successful!")
            else:
                print("Invalid withdrawal amount or insufficient funds!")
                
        elif choice == "3":
            account.display_balance()
            
        elif choice == "4":
            account.display_transactions()
            
        elif choice == "5":
            print("Thank you for banking with us!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
    
#Practice 4: Number Guessing Game

import random

def number_guessing_game():
    """Simple number guessing game"""
    print("=== Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100!")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}. Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try higher.")
            elif guess > secret_number:
                print("Too high! Try lower.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return
        
        except ValueError:
            print("Please enter a valid number!")
            continue
    
    print(f"😞 Game Over! The number was {secret_number}")

def main():
    while True:
        number_guessing_game()
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
    
#Practice 5: To-Do List Manager
class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        """Add a new task to the list"""
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!")
    
    def view_tasks(self):
        """View all tasks"""
        if not self.tasks:
            print("No tasks in your to-do list!")
            return
        
        print("\n=== Your To-Do List ===")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['task']}")
    
    def mark_completed(self, task_number):
        """Mark a task as completed"""
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed!")
        else:
            print("Invalid task number!")
    
    def delete_task(self, task_number):
        """Delete a task from the list"""
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted!")
        else:
            print("Invalid task number!")

def main():
    todo_list = TodoList()
    
    while True:
        print("\n=== To-Do List Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            
        elif choice == "2":
            todo_list.view_tasks()
            
        elif choice == "3":
            todo_list.view_tasks()
            try:
                task_num = int(input("Enter task number to mark completed: "))
                todo_list.mark_completed(task_num)
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == "4":
            todo_list.view_tasks()
            try:
                task_num = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_num)
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == "5":
            print("Goodbye! Stay organized! 📝")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
