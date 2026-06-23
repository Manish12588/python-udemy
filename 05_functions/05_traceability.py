def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100


orders = [100, 15, 200]
for price in orders:
    final_amout = add_vat(price, 10)
    print(f"Original: {price}, Final Price after VAT: {final_amout}")
