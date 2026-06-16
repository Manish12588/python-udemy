# Dictionary
chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(f"Recipe base: {chai_recipe['base']}")
print(f"chai recipe before del : {chai_recipe}")
del chai_recipe["liquid"]
print(f"chai recipe after del : {chai_recipe}")

# membership testing
print(f"Is 'sugar' in order? : {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

# print(f"Order details (keys) : {chai_order.keys()}")
# print(f"Order details (values) : {chai_order.values()}")

# popitem() just remove the item
last_item = chai_order.popitem()
print(f"last item :{last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated chai recipe :{chai_recipe}")

chai_size = chai_order["size"]
print(f"Chai size is: {chai_size}")

customer_note = chai_order.get("note", "No note available")
print(f"Customer note is: {customer_note}")


