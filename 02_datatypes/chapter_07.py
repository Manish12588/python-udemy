# Tuples
# tuples comees with () parantheses
# tuples are immutable

masala_spices = ("cardamom", "cloves", "cinnamon")

# How to extract the tuples value and add into variables
# I should know the counts before extracting it into variables
(spice1, spice2, spice3) = masala_spices
print(f"Main masala soices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2, 1  # 2 will assign to ginger_ratio
print(f"Ratio is for G {ginger_ratio}, and C: {cardamom_ratio}")

# Now if you wanted to switch the value in between you can easily do that
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ratio is for G {ginger_ratio}, and C: {cardamom_ratio}")

# membership testing
# in works with tuples

print(f"Is ginger in masala_spices? {'ginger' in masala_spices}")  # False
print(f"Is cinnamon in masala_spices? {'cinnamon' in masala_spices}")  # True
