flavours = ["ginger", "out of stock", "Lemon", "discountinued", "tulsi"]

for flavour in flavours:
    if flavour == "out of stock":
        continue
    if flavour == "discountinued":
        print(f"item discontinued.")
        break
    print(f"{flavour} item found in list")

print(f"outside the for loop")
