import pandas as pd
import numpy as np
import matplotlib.pyplot as mtlp

data = [
    {"name": "Apple", "description": "Food & Fruit", "price": 0.49},
    {"name": "Banana", "description": "Food & Fruit", "price": 0.35},
    {"name": "Orange", "description": "Food & Fruit", "price": 0.60},
    {"name": "Milk", "description": "Dairy Products", "price": 3.99},
    {"name": "Bread", "description": "Bakery", "price": 2.50},
    {"name": "Eggs", "description": "Dairy & Poultry", "price": 8.90},
    {"name": "Rice", "description": "Grains", "price": 24.99},
    {"name": "Beans", "description": "Grains", "price": 7.49},
    {"name": "Chicken Breast", "description": "Meat", "price": 18.90},
    {"name": "Coffee", "description": "Beverages", "price": 15.75},
]

print("\nProducts with original price: ")
print(pd.DataFrame(data))

# Extract prices and apply 10% off
prices = np.array([item["price"] for item in data]) * 0.9

# Update original vector
for item, new_price in zip(data, prices):
    item["price"] = round(new_price, 2)

df = pd.DataFrame(data)

print("\nProducts with 10% off: ")
print(df)

# Pandas use NumPy to do operations
print(f"\nAverage of prices: {df["price"].mean():,.2f}")

# Creating a column chart with series of data frame
mtlp.barh(df["description"], df["price"])
mtlp.show()