"""factorial
    """


def factorial(number):
    """this functions calculates the factorial for a given number

    Args:
        value (_integer_): _we pass this value to the functions to
        calculate the factorial of it_
    """
    if number == 1:
        return 1
    return number * factorial(number - 1)


print(factorial(4))
