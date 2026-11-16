import sqlite3

# Creating connection with SQLite DB
connection = sqlite3.connect("./public/data/examples/products.db")

cursor = connection.cursor()

# Creating table within DB if it not exits there
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id_product INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price INTEGER
)
""")

# cursor.execute(
#     "DELETE FROM products"
#     )

# data = [
#     {"name": "Notebook Dell Inspiron", "description": "Category: Electronics", "price": 3499.90},
#     {"name": "Wireless Mouse Logitech M170", "description": "Category: Electronics", "price": 79.90},
#     {"name": "Mechanical Keyboard Redragon Kumara", "description": "Category: Electronics", "price": 249.90},
#     {"name": "Samsung 24'' Monitor", "description": "Category: Electronics", "price": 899.90},
#     {"name": "Office Chair", "description": "Category: Furniture", "price": 599.90},
#     {"name": "Water Bottle 1L", "description": "Category: Home & Kitchen", "price": 24.90},
#     {"name": "LED Desk Lamp", "description": "Category: Home & Office", "price": 89.90},
#     {"name": "Coffee Maker", "description": "Category: Home Appliances", "price": 199.90},
#     {"name": "Bluetooth Headphones", "description": "Category: Audio", "price": 299.90},
#     {"name": "External SSD 1TB", "description": "Category: Storage", "price": 549.90},
# ]

# for product in data:
#     cursor.execute(
#         "INSERT INTO products (name, description, price) VALUES (?, ?, ?)", 
#         (product["name"], product["description"], product["price"])
#     )

# Selecting all registers from products
cursor.execute("SELECT * FROM products")

data = cursor.fetchall()

print("\nProducts registered:")
for row in data:
    print(row)

# Transactiion COMMIT to confirm operations
connection.commit()

# Finishing connection with DB
connection.close()