order_amout = int(input("Enter the order amout: "))
# print(f"order amout: {type(order_amout)}")

# turnery operator
delivery_fees = 0 if order_amout > 300 else 30
print(f"Delivery fees is: {delivery_fees}")
