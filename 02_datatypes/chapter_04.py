is_boiling = True
stir_count = 5
total_actions = is_boiling + stir_count  # upcasting
print(f"Total actions => {total_actions}")
# True is represented as 1
# False is represented as 0

milk_present = 0  # None, 11, Manish all give flase result
print(f"Is milk there => {bool(milk_present)}")

# Logical operations -> and, or , not
# and -> tea and cookies\
# or -> tea of coffe
# not ->
water_hot = True
tea_added = True
can_server = water_hot and tea_added
print(f"Can server chai? => {can_server}")
