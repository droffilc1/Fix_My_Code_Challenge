#!/usr/bin/python3
"""Square module"""


class Square():
    """Square class"""
    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """ Initialize data  """
        self.width = width
        self.height = height

        if self.height != self.width:
            self.height = self.width
        if self.width != self.height:
            self.width = self.height

    @property
    def width(self):
        """Getter method for width
        Setter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height
        Setter method for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

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

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimiter_of_my_square())
