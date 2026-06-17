snack = input("Enter your preferred snack: ").lower()
print(f"user said: {snack}")

if snack == "cookies" or snack == "samosa":
    print(f"Order confirmed! :{snack}")
else:
    print(f"Sorry, we only serve cookies and samosa")
