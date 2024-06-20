#function for each arithmetic operation 
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y 
def multiply(x, y):
    return x * y 
def divide(x, y):
    if y == 0:
        return "error: division by zero"
    return x / y
#dictionary mapping opeartors to functions
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
#user input
num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))
operator = input("enter the operator(+, -, *, /):")
#perform calculation based on operator if operator in operations:
result = operations[operator](num1, num2)
print(f"the results of {num1} {operator} {num2} is {result}")
else:
print("invalid operator. please enter a valid operator(+, -, *, /)")

