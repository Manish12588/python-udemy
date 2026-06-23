# def pure_chai(cups):  # pure function
#     return cups * 10


# total_chai = 0


# Not recommended
# def impure_chai(cups):
#     global total_chai
#     total_chai += cups


# Recursive function
def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n - 1)  # Recursion


print(pour_chai(3))


# Anonymous function
chai_type = ["light", "kadak", "giner", "kadak"]

strong_chai = list(filter(lambda chai: chai != "kadak", chai_type))
print(strong_chai)
