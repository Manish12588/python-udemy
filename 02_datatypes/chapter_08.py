# Mutable
# => List is similar to Array

ingredients = ["water", "milk", "balck tea"]

# Now if you forgot any ingredients and wanted to add you can easily add but in tuples you have to edit the tuples.
ingredients.append("sugar")
print(f"Ingredients : {ingredients}")

# remove from List
ingredients.remove("water")
print(f"Ingredients : {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]
chai_ingredients.extend(spice_options)
print(f"chai_ingredients : {chai_ingredients}")

# insert you have to give the position where you wanted to add the item in list
chai_ingredients.insert(2, "Black tea")
print(f"chai_ingredients : {chai_ingredients}")

# more methods in list
# pop() -> pop will remove the last element from list, it return the deleted item from list
deletedItem = chai_ingredients.pop()
print(f"chai_ingredients : {chai_ingredients}")

# reverse
chai_ingredients.reverse()
print(f"chai_ingredients reverse order : {chai_ingredients}")

# sorting
chai_ingredients.sort()
print(f"chai_ingredients sorted order : {chai_ingredients}")

# max and min
sugar_labels = [1, 2, 3, 4, 5]
print(f"Maximum sugar label :{max(sugar_labels)}")
print(f"Minimum sugar label :{min(sugar_labels)}")

# Operator overloading
base_liquid = ["water", "milk"]
extra_flavor = ["giger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"full_liquid_mix: {full_liquid_mix}")

strong_brew = ["black tea"] * 3
print(f"Liquid Mix: {strong_brew}")

strong_brew_2 = ["black tea", "water"] * 3
print(f"Liquid Mix brew: {strong_brew_2}")

#  convert to bytearray
raw_spice_data = bytearray("CINNAMON".encode("utf-8"))
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"raw_spice_data: {raw_spice_data}")
