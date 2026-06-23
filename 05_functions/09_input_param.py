# chai = "ginger chai"


# def prepare_chai(order):
#     print(f"Preparing: {order}")


# prepare_chai(chai)
# print(chai)

# =================
# chai = [1, 2, 3]


# def edit_chai(cup):
#     chai[1] = 42


# edit_chai(chai)
# print(f"chai: {chai}")


# =========================
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)


make_chai("Darjeeling", "Yes", "Low")  # Positional
make_chai(tea="Green", sugar="Low", milk="Yes")  # Keywords


def special_chai(*ingredients, **extras):  # args and kwargs (key value)
    print("Ingredients", ingredients)  # Ingredients gets the tuples
    print("Extras", extras)  # dictionary


special_chai("Cinnamon", "Cardmom", sweetner="Honey", foam="Yes")


# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)


def chai_order(order=None):
    if order is None:
        order = []
    print(order)


chai_order()
chai_order()
