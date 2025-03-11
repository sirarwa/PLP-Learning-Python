# Get user input for two numbers and an operator
num1 = float(input("Enter the first number: "))  # Accepts first number from the user
num2 = float(input("Enter the second number: "))  # Accepts second number from the user
operator = input("Enter an operation (+, -, *, /): ")  # Accepts mathematical operation from the user
# Perform the operation based on the user input
if operator == '+':
    # Perform addition
    result = num1 + num2  
    print(f"{num1} + {num2} = {result}")
     # Perform subtraction
elif operator == '-':
    result = num1 - num2 
    print(f"{num1} - {num2} = {result}")
    # Perform multiplication
elif operator == '*':
    result = num1 * num2  
    print(f"{num1} * {num2} = {result}")
    # Check to prevent division by zero
elif operator == '/':
    if num2 != 0:  
        # Perform division
        result = num1 / num2  
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator! Please enter one of +, -, *, or /.")
