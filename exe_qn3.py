# Creating a list of product names and prices
products = {
    "Product A": 10.10,
    "Product B": 24.10,
    "Product C": 50.10,
    "Product D": 15.10,
    "Product E": 80.10
}

# Displaying the product catalog in a neat table format using f-strings

for product, price in products.items():
    print(f"{product:<10} | ${price:.2f}")
