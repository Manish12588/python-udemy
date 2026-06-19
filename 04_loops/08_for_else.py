staff = [("Amit", 16), ("Raj", 17), ("Zara", 15)]  # Tuple inside list

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage staff")
        break
else:  # fall back logic in case we didn't find any results from for loop
    print(f"No one is eligible to manage the staff")
