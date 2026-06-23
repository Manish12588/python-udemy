# { expression for item in iterable if condition }

favourite_chai = [
    "Masala chai",
    "Green tea",
    "Masala chai",
    "Lemon tea",
    "Green tea",
    "Elachai chai",
]

# Find out how many unique chai in given list, it's same as list but if part is not required sometime
unique_tea = {chai for chai in favourite_chai}
print(unique_tea)


# complex example
recipes = {
    "Masala chai": ["Ginger", "Cardamom", "Clove"],
    "Elaichi chai": ["Cardamom", "milk"],
    "Spicy chai": ["Ginger", "black pepper", "Clove"],
}

# Find the unique spices,
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)
