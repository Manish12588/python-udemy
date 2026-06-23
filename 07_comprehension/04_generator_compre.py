# Generator are generally used to saving memory
# (expression for item in iterable if condition )
# [x for x in items] -> Make entire list in memory
# (x for x in items) -> Like a stream

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

# find out toal cup sold any sale above 5 rupees and get the total
total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)
