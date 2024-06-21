import math
def calculate_N(x):
    numerator = (x**4 - x**3 + x**2 - x) 
    denominator = (x + 1)**2 
    return numerator / denominator - math.sqrt(x)
x = float(input("enter the vaule of x: "))
N = calculate_N(x)
print("the value of N IS:", N)
