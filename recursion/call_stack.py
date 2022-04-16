"""Call stack
    """


def func_three():
    """function three does something
    """
    print('Three')


def func_two():
    """function two calls function three and then does something
    """
    func_three()
    print('Two')


def func_one():
    """function one calls function two and then does something
    """
    func_two()
    print('One')


func_one()
