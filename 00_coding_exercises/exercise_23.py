"""
Smart Inventory Filter

You are building a Smart Inventory Filter for a retail store.

Tasks:
Process a list of product dictionaries, where each product has name, price, and category.
Use different types of comprehensions to:
Extract names of products priced below ₹500 using list comprehension.
Extract all unique categories using set comprehension.
Create a name-to-price mapping using dictionary comprehension.
Generate a list of discounted prices using a generator expression and convert it to a list.
Return all four outputs as a tuple.
"""

items = [
    {"name": "Notebook", "price": 250, "category": "Stationery"},
    {"name": "Pen", "price": 100, "category": "Stationery"},
    {"name": "Bag", "price": 1200, "category": "Accessories"},
    {"name": "Bottle", "price": 400, "category": "Utensils"},
]

# List comprehension
# [expression for item in iterable if condition]

# 1. Extract names of products priced below ₹500 using list comprehension.

price_below_500 = [item["name"] for item in items if item["price"] < 500]
print("Product below 500 => ", price_below_500)

# 2. Extract all unique categories using set comprehension.
unique_category = {item["category"] for item in items}
print("Unique Product category => ", unique_category)

# 3.Create a name-to-price mapping using dictionary comprehension.
name_to_price = {item["name"]: item["price"] for item in items}
print("Name to Price mapping => ", name_to_price)

# 4.Generate a list of discounted prices using a generator expression and convert it to a list.
discounted_price = list((int(item["price"] * 0.9) for item in items))
print("Item on discounted price => ", discounted_price)
