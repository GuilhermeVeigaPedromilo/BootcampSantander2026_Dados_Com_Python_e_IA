import pandas as pd

data = [
    {"name": "Apple", "description": "Category: Food & Fruit", "price": 0.49},
    {"name": "Banana", "description": "Category: Food & Fruit", "price": 0.35},
    {"name": "Orange", "description": "Category: Food & Fruit", "price": 0.60},
    {"name": "Milk", "description": "Category: Dairy Products", "price": 3.99},
    {"name": "Bread", "description": "Category: Bakery", "price": 2.50},
    {"name": "Eggs", "description": "Category: Dairy & Poultry", "price": 8.90},
    {"name": "Rice", "description": "Category: Grains", "price": 24.99},
    {"name": "Beans", "description": "Category: Grains", "price": 7.49},
    {"name": "Chicken Breast", "description": "Category: Meat", "price": 18.90},
    {"name": "Coffee", "description": "Category: Beverages", "price": 15.75},
]

# Creating a DataFrame with data
df = pd.DataFrame(data)
print(df)