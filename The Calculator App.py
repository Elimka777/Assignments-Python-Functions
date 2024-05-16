#The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

#Task 1: Create functions for each arithmetic operation.
#Task 2: Implement user input to receive numbers and an operation choice.
#Task 3: Ensure your program can handle division by zero and other potential errors.
def add_num(a, b):
 return a+b
def subtract_num(a,b):
 return a-b
def multiply_num(a,b):
 return a*b
def divide_num(a,b):
 return a/b

def get_user_input():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Choose operation (+, -, *, /): ")
            
            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation. Please choose from +, -, *, /")
                continue
            
            return num1, num2, operation
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
def calculator():
    while True:
        num1, num2, operation = get_user_input()
        
        if operation == '+':
            result = add_num(num1, num2)
        elif operation == '-':
            result = subtract_num(num1, num2)
        elif operation == '*':
            result = multiply_num(num1, num2)
        elif operation == '/':
            result = divide_num(num1, num2)
        
        print("Result:", result)
        
        if input("Do you want to perform another calculation? (yes/no): ").lower() != 'yes':
            break
calculator()