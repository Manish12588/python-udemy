sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Second Initial sugar: {sugar_amount}")

# now sugar_amount is pointing to 12, so changing the reference not value

# How to check the identity
print(f"Id of 2: {id(2)}") #11370064
print(f"Id of 12: {id(12)}") #11370384

