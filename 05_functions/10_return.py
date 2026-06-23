# def make_chai():
#     return "Here is masala chai"


# return_value = make_chai()

# print(return_value)


def idle_chai_wala():
    pass


print(idle_chai_wala())  # Return None


def sold_cups():
    return 120


total = sold_cups()
print(total)


def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"


print(chai_status(0))
print(chai_status(5))


# Return multiple value
def chai_report():
    return 100, 200  # sold, remaining


sold, remaining = chai_report()
print(f"Sold: {sold}")
print(f"Remaining: {remaining}")
