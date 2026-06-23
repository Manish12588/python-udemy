def chai_flavor(flavour="Masala"):
    """it return the flavor of chai."""  # It has to be very first line (documentation)
    return flavour


print(chai_flavor.__doc__)  # It return the documentation
print(chai_flavor.__name__)  # it return the name of function


def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa
    :param: chai: Number of chai cups (10 rupee each)
    :param: samosa: Number of samosa (15 rupee each)
    :return: (total amount, thankyou message as string)
    """
    total = chai * 10 + samosa * 15
    return total, "Thank you for visiting chaicode.com"


totalBill = generate_bill(2, 1)
print(totalBill)
