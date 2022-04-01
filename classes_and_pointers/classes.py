"""classes
    """


class Cookie:
    """creating a cookie class
    """

    def __init__(self, color):
        self.color = color

    def get_color(self):
        """it returns the color for a particular cookie

        Returns:
            _type_: _description_
        """
        return self.color

    def set_color(self, color):
        """this will change the color for a particular cookie

        Args:
            color (_type_): _description_
        """
        self.color = color


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie One is:', cookie_one.get_color())
print('Cookie Two is:', cookie_two.get_color())

cookie_one.set_color('red')

print('Cookie One is now:', cookie_one.get_color())
print('Cookie Two is still:', cookie_two.get_color())
