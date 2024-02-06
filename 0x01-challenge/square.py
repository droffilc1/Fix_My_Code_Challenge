#!/usr/bin/python3
"""square.py"""


class Square:
    """Square class"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initialize data  """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimiter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Print the square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimiter_of_my_square())
