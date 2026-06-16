# Integer


black_tea_grams = 14
ginger_gram = 3
total_gram = black_tea_grams + ginger_gram
print(f"total gram => {total_gram}")

remaing_tea = black_tea_grams * ginger_gram
print(f"Total gram of remaining tea is => {remaing_tea}")

milk_liters = 7
servings = 4
milk_per_serving = milk_liters / servings
print(f"Milk per serving is {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot => {bags_per_pot}")

total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"Left over C pods => {leftover_pods}")

base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength**scale_factor
print(f"Scaled Flavour strength {powerful_flavour}")  # 2*2*2

total_tea_leave_harvested = 1_000_000_000
print(f"Total leave harvested => {total_tea_leave_harvested}")
