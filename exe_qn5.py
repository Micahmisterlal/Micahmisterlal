# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user for the operation they want to perform
operation = input("Choose an operation (addition, subtraction, multiplication, division): ")

# Perform the chosen operation on the numbers
if operation == "addition":
    result = num1 + num2
elif operation == "subtraction":
    result = num1 - num2
elif operation == "multiplication":
    result = num1 * num2
elif operation == "division":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Division by zero is not allowed"
else:
    result = "Invalid operation"

# Print the result
print(f"Result of {operation} is: {result}")