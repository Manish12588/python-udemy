# list [], dictionary {key:value}

users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 120, "coupon": "F10"},
    {"id": 3, "total": 150, "coupon": "P50"},
]

discounts = {"P20": (0.2, 0), "F10": (0.5, 0), "P50": (0, 10)}

for user in users:
    percent, fix = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fix
    print(
        f"{user["id"]} paid {user["total"]} and got the discount for next visit or rupees {discount}"
    )
