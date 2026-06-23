# {expression for item in iterable if condition}
# expression: should return the key:value pair

tea_prices = {"Masala chai": 40, "Green tea": 50, "Lemon tea": 200}

# Needs to convert. the price in dollar
tea_price_usd = {tea: price / 80 for tea, price in tea_prices.items()}
print(tea_price_usd)
