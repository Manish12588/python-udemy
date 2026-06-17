cupSize = input("Choose your cup size(small/medium/large): ").lower()

if cupSize == "small":
    print("Price is 10 ruppes.")
elif cupSize == "medium":
    print("Price is 15 ruppes.")
elif cupSize == "large":
    print("Price is 20 ruppes.")
else:
    print("Unknown cup size")
